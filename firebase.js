// firebase.js
// Shared code that gets injected via content_scripts into all pages

const FIREBASE_CONFIG = {
  projectId: "joyboy-b6f27", 
  collectionName: "applications"
};

/**
 * Saves a JSON object to Firestore using the Firestore REST API.
 * Ensure your Firestore rules allow unauthenticated writes, or pass an Auth token if secured.
 */
async function saveToFirestore(data) {
  if (FIREBASE_CONFIG.projectId === "YOUR_PROJECT_ID") {
    throw new Error("Missing Firebase Config: Please update the Project ID in firebase.js");
  }

  // 🆔 Get Multi-User Identity from Storage
  const identity = await chrome.storage.local.get(['applisync_user_id', 'applisync_token']);
  const uid = identity.applisync_user_id;
  const token = identity.applisync_token;

  if (!uid || !token) {
    throw new Error("AppliSync Identity Error: Please log in to the web dashboard first to sync your account with the extension.");
  }

  // Inject current user ID into the data
  data.userId = uid;

  // Firestore REST API Endpoint
  const url = `https://firestore.googleapis.com/v1/projects/${FIREBASE_CONFIG.projectId}/databases/(default)/documents/${FIREBASE_CONFIG.collectionName}`;
  
  // Transform standard JSON into Firestore's required REST format
  const fields = {};
  for (const [key, value] of Object.entries(data)) {
    if (value === null || value === undefined) {
      fields[key] = { nullValue: null };
    } else if (Array.isArray(value)) {
      fields[key] = {
        arrayValue: {
          values: value.map(v => ({ stringValue: String(v) }))
        }
      };
    } else if (typeof value === "object" && !Array.isArray(value)) {
      // Handles user_inputs object
      const mapValue = { fields: {} };
      for (const [k, v] of Object.entries(value)) {
        mapValue.fields[k] = { stringValue: String(v) };
      }
      fields[key] = { mapValue };
    } else if (typeof value === "number") {
      fields[key] = { doubleValue: value };
    } else {
      fields[key] = { stringValue: String(value) };
    }
  }

  const payload = { fields };

  const response = await fetch(url, {
    method: 'POST',
    headers: { 
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}` // 🛡️ Secure Authorization
    },
    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`Firestore HTTP Error ${response.status}: ${errorText}`);
  }

  return await response.json();
}

// Attach to window object so content.js can access it
window.saveToFirestore = saveToFirestore;
