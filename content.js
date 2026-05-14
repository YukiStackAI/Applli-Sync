// content.js
// V2.2 "Auto-Pilot": Automatic Multi-Step Extraction & HR Intelligence

// AI_API_KEY is provided by extension-config.js
const AI_API_URL = "https://api.groq.com/openai/v1/chat/completions";

let sessionData = {
  trackedInputs: {},
  capturedTexts: [],
  isTracking: false
};

const SESS_KEY = `tab_session_data`;
let lastTextHash = "";

async function init() {
  const stored = await chrome.storage.local.get(SESS_KEY);
  if (stored[SESS_KEY] && stored[SESS_KEY].isTracking) {
    sessionData = stored[SESS_KEY];
    bindListeners();
    startAutoPilot();
    console.log("Agent Auto-Pilot Active.");
  }
}

async function syncToStorage() {
  await chrome.storage.local.set({ [SESS_KEY]: sessionData });
}

// Deduplication Logic
function getTextHash(text) {
  // Simple length + first 100 chars hash
  return `${text.length}_${text.substring(0, 100)}`;
}

function captureSnapshot(isAuto = false) {
  const currentText = document.body.innerText;
  const currentHash = getTextHash(currentText);

  // Skip if text hasn't changed (prevents redundant auto-saves)
  if (isAuto && currentHash === lastTextHash) return;
  lastTextHash = currentHash;

  // Sync inputs
  const inputs = document.querySelectorAll("input, textarea, select");
  inputs.forEach(input => handleInputEvent({ target: input }));

  sessionData.capturedTexts.push(currentText);
  syncToStorage();
  
  if (isAuto) console.log("Auto-Pilot: Snapshot captured automatically.");
}

function handleInputEvent(e) {
  const input = e.target;
  if (input.tagName === 'INPUT' || input.tagName === 'TEXTAREA' || input.tagName === 'SELECT') {
    if (input.type === 'password' || input.type === 'hidden') return;
    let name = input.name || input.id || input.placeholder;
    if (!name && input.previousElementSibling && input.previousElementSibling.tagName === 'LABEL') {
      name = input.previousElementSibling.innerText.trim();
    }
    if (!name) name = "field_" + (input.className.split(' ')[0] || "unknown");
    
    if (input.value) {
      sessionData.trackedInputs[name] = input.value;
      syncToStorage();
    }
  }
}

// Auto-Pilot Logic: Watch for URL or DOM changes
function startAutoPilot() {
  // Listen for URL changes (Single Page Apps)
  window.addEventListener('popstate', () => captureSnapshot(true));
  
  // Watch for major DOM changes (e.g., "Next" button reveals new form section)
  let timeout;
  const observer = new MutationObserver(() => {
    clearTimeout(timeout);
    timeout = setTimeout(() => captureSnapshot(true), 2000); // 2s debounce
  });

  observer.observe(document.body, { childList: true, subtree: true });
}

function bindListeners() {
  document.addEventListener('input', handleInputEvent, true);
  document.addEventListener('change', handleInputEvent, true);
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "START_TRACKING") {
    sessionData = { trackedInputs: {}, capturedTexts: [], isTracking: true };
    syncToStorage().then(() => {
      captureSnapshot();
      bindListeners();
      startAutoPilot();
      sendResponse({ success: true });
    });
    return true;
  }

  if (request.action === "CAPTURE_STEP") {
    captureSnapshot();
    sendResponse({ success: true });
    return false;
  }
  
  if (request.action === "FINISH_AND_SAVE") {
    processFinalSave(request.notes)
      .then(() => sendResponse({ success: true }))
      .catch((err) => sendResponse({ success: false, error: err.message }));
    return true; 
  }
});

async function processFinalSave(userNotes) {
  captureSnapshot(); // One last grab
  const consolidatedText = sessionData.capturedTexts.join("\n\n--- NEXT PAGE ---\n\n");
  const jobUrl = window.location.href;

  const aiData = await extractJobDataViaAI(consolidatedText, sessionData.trackedInputs, userNotes, jobUrl);
  
  if (window.saveToFirestore) {
    await window.saveToFirestore(aiData);
  } else {
    throw new Error("Local DB module error.");
  }
  
  sessionData = { trackedInputs: {}, capturedTexts: [], isTracking: false };
  await syncToStorage();
}

async function extractJobDataViaAI(rawText, userInputs, userNotes, jobUrl) {
  const currentDate = new Date().toISOString().split('T')[0];
  
  const systemPrompt = `You are a Senior Full-Stack Intelligence Agent. Extract metadata from job pages.
STRICT JSON OUTPUT ONLY.

JSON STRUCTURE:
{
  "company_name": "",
  "job_title": "",
  "job_description": "",
  "date_posted": "",
  "date_applied": "${currentDate}",
  "experience_required": "Fresher",
  "skills": [],
  "hr_name": null,
  "hr_linkedin_url": null,
  "hr_designation": null,
  "location": "",
  "work_mode": "Onsite",
  "job_type": "Full-time",
  "salary_range": null,
  "application_url": "${jobUrl}",
  "platform": "NA",
  "company_website": "NA",
  "status": "Applied",
  "notes": "${userNotes || ""}",
  "user_inputs": {}
}

SPECIAL INSTRUCTIONS:
1. **HR/Poster Intelligence**: Search for mentions of "Hiring Manager", "Posted by", "Recruiter", or any specific person's name associated with publishing the JD. Extract their name, link, and role.
2. **Platform Tracking**: Identify the recruitment platform (e.g., LinkedIn, Indeed, Naukri, Wellfound, Glassdoor, or Direct Company Site).
3. work_mode: "Remote", "Hybrid", or "Onsite".
4. salary_range: Extract figures (e.g. "$100k-$120k" or "£50,000").
4. **Missing Data**: If any field (HR name, salary, etc.) is NOT found in the text, you MUST return "NA" for that field. Do not return null.
5. Merge all form entries from user_inputs accurately.`;

  const userMessage = `CONTEXTUAL_TEXT:
${rawText.substring(0, 30000)}

FORM_DATA_CAPTURED:
${JSON.stringify(userInputs, null, 2)}`;

  const response = await fetch(AI_API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${AI_API_KEY}`
    },
    body: JSON.stringify({
      model: "llama-3.3-70b-versatile",
      messages: [
        { role: "system", content: systemPrompt },
        { role: "user", content: userMessage }
      ],
      temperature: 0.1
    })
  });

  if (!response.ok) throw new Error(`AI Error: ${response.status}`);

  const data = await response.json();
  let content = data.choices[0].message.content.trim();
  if (content.includes("```")) content = content.replace(/```json|```/g, "").trim();

  const parsed = JSON.parse(content);
  parsed.user_inputs = { ...parsed.user_inputs, ...userInputs };
  return parsed;
}

// External Auth Sync: Listen for messages from the AppliSync Dashboard
window.addEventListener("message", (event) => {
  // We only care about our specific auth sync message
  if (event.data && event.data.type === 'APPLISYNC_AUTH_SYNC') {
    const { uid, token } = event.data;
    chrome.storage.local.set({ 
      'applisync_user_id': uid,
      'applisync_token': token 
    }, () => {
      console.log("AppliSync: User identity synchronized from dashboard.");
    });
  }
});

init();
