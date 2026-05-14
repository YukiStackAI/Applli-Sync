const fs = require('fs');
const path = require('path');

// 1. Generate js/firebase-config.js
const firebaseConfigContent = `// Generated during build
const firebaseConfig = {
    apiKey: "${process.env.FIREBASE_API_KEY || ''}",
    authDomain: "${process.env.FIREBASE_AUTH_DOMAIN || ''}",
    projectId: "${process.env.FIREBASE_PROJECT_ID || ''}",
    storageBucket: "${process.env.FIREBASE_STORAGE_BUCKET || ''}",
    messagingSenderId: "${process.env.FIREBASE_MESSAGING_SENDER_ID || ''}",
    appId: "${process.env.FIREBASE_APP_ID || ''}",
    measurementId: "${process.env.FIREBASE_MEASUREMENT_ID || ''}"
};
export default firebaseConfig;
`;

const jsDir = path.join(process.cwd(), 'js');
if (!fs.existsSync(jsDir)) fs.mkdirSync(jsDir);
fs.writeFileSync(path.join(jsDir, 'firebase-config.js'), firebaseConfigContent);

// 2. Generate extension-config.js
const extensionConfigContent = `// Generated during build
const AI_API_KEY = "${process.env.GROQ_AI_API_KEY || ''}";
`;
fs.writeFileSync(path.join(process.cwd(), 'extension-config.js'), extensionConfigContent);

console.log('Build: Configuration files generated successfully.');
