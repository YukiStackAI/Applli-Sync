// popup.js
document.addEventListener('DOMContentLoaded', async () => {
  const startBtn = document.getElementById('startBtn');
  const captureBtn = document.getElementById('captureBtn');
  const saveBtn = document.getElementById('saveBtn');
  const notesArea = document.getElementById('notesArea');
  const statusText = document.getElementById('statusText');
  const pulseIcon = document.getElementById('pulseIcon');
  const stepCountEl = document.getElementById('stepCount');

  const SESS_KEY = `tab_session_data`;

  async function refreshUI() {
    const data = await chrome.storage.local.get(SESS_KEY);
    const session = data[SESS_KEY] || { isTracking: false, capturedTexts: [] };

    if (session.isTracking) {
      startBtn.style.display = 'none';
      captureBtn.style.display = 'flex';
      saveBtn.style.display = 'flex';
      notesArea.style.display = 'block';
      pulseIcon.style.display = 'block';
      stepCountEl.innerText = session.capturedTexts.length;
      statusText.innerText = "Auto-Pilot Active";
      statusText.style.color = "#10b981";
    } else {
      startBtn.style.display = 'flex';
      captureBtn.style.display = 'none';
      saveBtn.style.display = 'none';
      notesArea.style.display = 'none';
      pulseIcon.style.display = 'none';
      statusText.innerText = "Agent Offline";
      statusText.style.color = "#94a3b8";
    }
  }

  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (tab) await refreshUI();

  startBtn.addEventListener('click', async () => {
    statusText.innerText = "Deploying...";
    chrome.tabs.sendMessage(tab.id, { action: "START_TRACKING" }, async (response) => {
      if (chrome.runtime.lastError) {
        statusText.innerText = "Refresh the page!";
        return;
      }
      setTimeout(refreshUI, 200);
    });
  });

  captureBtn.addEventListener('click', async () => {
    statusText.innerText = "Capturing...";
    chrome.tabs.sendMessage(tab.id, { action: "CAPTURE_STEP" }, async (response) => {
      if (chrome.runtime.lastError) {
        statusText.innerText = "Refresh the page!";
        return;
      }
      setTimeout(refreshUI, 200);
    });
  });

  saveBtn.addEventListener('click', async () => {
    statusText.innerText = "Finalizing...";
    saveBtn.disabled = true;
    const notes = notesArea.value;

    chrome.tabs.sendMessage(tab.id, { action: "FINISH_AND_SAVE", notes: notes }, async (response) => {
      saveBtn.disabled = false;
      if (chrome.runtime.lastError) {
        statusText.innerText = "Refresh the page!";
        return;
      }
      if (response && response.success) {
        statusText.innerText = "Success! 🎉";
        setTimeout(refreshUI, 2000);
      } else {
        statusText.innerText = "Save Failed";
      }
    });
  });
});
