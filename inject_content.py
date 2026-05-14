import os
import re

# Read the index.html to extract styles, navbar, and footer
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract head
head_match = re.search(r'(<head>.*?</head>)', html, re.DOTALL)
head = head_match.group(1) if head_match else '<head><title>AppliSync</title></head>'

# Extract navbar
nav_match = re.search(r'(<!-- ═══ Navbar ═══ -->.*?)</nav>', html, re.DOTALL)
nav = nav_match.group(1) + '</nav>' if nav_match else ''

# Extract footer
footer_match = re.search(r'(<!-- ═══ Footer ═══ -->.*?)</body>', html, re.DOTALL)
footer = footer_match.group(1) if footer_match else '</footer>'

def get_base_template(content_html):
    return f"""<!DOCTYPE html>
<html lang="en">
{head}
<body>
    {nav}

    <!-- ═══ Main Content ═══ -->
    <main style="padding: 120px 2rem 80px; min-height: 80vh; max-width: 1200px; margin: 0 auto;">
        {content_html}
    </main>

    {footer}
</body>
</html>
"""

pages = {}

# 1. Contact Page
pages["contact.html"] = '''
        <div class="fade-up" style="display: flex; gap: 4rem; flex-wrap: wrap;">
            <!-- Contact Form -->
            <div style="flex: 2; min-width: 300px; background: var(--bg-card); padding: 3rem; border-radius: 24px; border: 1px solid var(--border); box-shadow: 0 12px 24px rgba(0,0,0,0.05);">
                <h1 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 1rem;">Contact <span style="color: var(--accent)">Us</span></h1>
                <p style="color: var(--text-secondary); margin-bottom: 2rem;">Have questions about your tracking dashboard, need support, or looking for a partnership? Send us a message.</p>
                
                <form id="contactForm" onsubmit="submitForm(event)">
                    <input type="text" name="name" class="auth-input" placeholder="Full Name" required>
                    <input type="email" name="email" class="auth-input" placeholder="Email Address" required>
                    
                    <select name="subject" class="auth-input" required style="appearance: none; background-color: var(--bg-primary);">
                        <option value="" disabled selected>Select a Subject</option>
                        <option value="General Inquiry">General Inquiry</option>
                        <option value="Bug Report">Bug Report</option>
                        <option value="Feature Request">Feature Request</option>
                        <option value="Partnership">Partnership</option>
                    </select>
                    
                    <textarea name="message" class="auth-input" placeholder="Your Message" rows="5" style="resize: vertical;" required></textarea>
                    <button type="submit" id="submitBtn" class="btn-primary-lg" style="width: 100%; margin-top: 1rem;">Send Message</button>
                </form>
            </div>
            
            <!-- Sidebar Info -->
            <div style="flex: 1; min-width: 300px; padding: 2rem;">
                <h3 style="font-size: 1.5rem; margin-bottom: 1.5rem;">Reach Out Directly</h3>
                <div style="margin-bottom: 2rem;">
                    <p style="color: var(--text-secondary); margin-bottom: 0.5rem;"><strong>Response Time:</strong></p>
                    <p style="color: var(--accent);">We typically reply within 24–48 hours.</p>
                </div>
                
                <div style="margin-bottom: 2rem;">
                    <p style="color: var(--text-secondary); margin-bottom: 1rem;"><strong>Quick Links:</strong></p>
                    <a href="faq.html" style="display: block; margin-bottom: 0.5rem; color: var(--text-primary); font-weight: 600;">→ Read our FAQ</a>
                    <a href="support.html" style="display: block; margin-bottom: 0.5rem; color: var(--text-primary); font-weight: 600;">→ Visit Support Center</a>
                </div>
                
                <div style="margin-bottom: 2rem;">
                    <p style="color: var(--text-secondary); margin-bottom: 1rem;"><strong>Community:</strong></p>
                    <a href="https://github.com/ShubhamV2503/Applli-Sync" target="_blank" style="display: inline-block; padding: 8px 16px; background: var(--bg-card); border: 1px solid var(--border); border-radius: 8px; font-weight: 600;">GitHub Repository</a>
                </div>
            </div>
        </div>

        <script>
            function submitForm(event) {
                event.preventDefault();
                const form = event.target;
                const btn = document.getElementById('submitBtn');
                btn.textContent = 'Sending...';
                btn.disabled = true;

                fetch("https://formsubmit.co/ajax/smitshah3510@gmail.com", {
                    method: "POST",
                    headers: { 
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    body: JSON.stringify({
                        name: form.name.value,
                        email: form.email.value,
                        _subject: "AppliSync Contact: " + form.subject.value,
                        message: form.message.value,
                        _cc: "vishwakarmashubham.2503@gmail.com",
                        _template: "table"
                    })
                })
                .then(response => response.json())
                .then(data => {
                    window.location.href = "success.html";
                })
                .catch(error => {
                    console.log(error);
                    btn.textContent = 'Send Message';
                    btn.disabled = false;
                    alert('There was an error sending the message.');
                });
            }
        </script>
'''

# 2. Privacy Policy
pages["privacy-policy.html"] = '''
        <div class="fade-up" style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
            <h1 style="font-size: 3rem; font-weight: 800; margin-bottom: 1rem;">Privacy <span style="color: var(--accent)">Policy</span></h1>
            <p style="color: var(--text-secondary); margin-bottom: 3rem;">Last Updated: April 2026</p>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">1. Introduction</h2>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">Welcome to AppliSync. This Privacy Policy explains how we collect, use, and protect your data when you use our Chrome Extension and Web Dashboard. We are committed to transparency and enterprise-grade data security.</p>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">2. Data We Collect</h2>
            <ul style="color: var(--text-secondary); margin-bottom: 2rem; padding-left: 1.5rem;">
                <li><strong>Job Application Metadata:</strong> Company name, job title, salary, and experience required.</li>
                <li><strong>HR Intelligence Data:</strong> Recruiter names and LinkedIn profiles extracted from job posts.</li>
                <li><strong>Chrome Extension Data:</strong> DOM text and form inputs, temporarily cached in <code>chrome.storage.local</code> to assist with AI extraction.</li>
                <li><strong>Firebase Auth Data:</strong> Your Google, GitHub, or Email login information, and unique UID.</li>
                <li><strong>Contact Form Submissions:</strong> Data provided voluntarily via our support forms.</li>
            </ul>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">3. How We Use Your Data</h2>
            <ul style="color: var(--text-secondary); margin-bottom: 2rem; padding-left: 1.5rem;">
                <li>To populate your personal Firestore dashboard with your tracked applications.</li>
                <li>For AI parsing via the Groq API (LLaMA 3.3 70b). <em>Note: Text content from job pages is securely transmitted to Groq's servers for the sole purpose of metadata extraction.</em></li>
                <li>To synchronize your session securely between the browser extension and the web dashboard using <code>window.postMessage</code>.</li>
            </ul>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">4. Data Storage & Retention</h2>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">Your permanent application data is securely stored in Firebase Firestore under your unique, authenticated UID. Temporary data used during the extraction process is cached in <code>chrome.storage.local</code> and is cleared immediately after the application is saved to the cloud.</p>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">5. Third-Party Services Used</h2>
            <ul style="color: var(--text-secondary); margin-bottom: 2rem; padding-left: 1.5rem;">
                <li><strong>Firebase (Google):</strong> Used for secure Authentication and Database storage.</li>
                <li><strong>Groq API:</strong> Used for blazing-fast AI text parsing.</li>
                <li><strong>FormSubmit:</strong> Used to securely route contact form submissions to our team.</li>
            </ul>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">6. User Rights & Security</h2>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">You have the right to access, correct, or delete your data at any time via your dashboard. Security is enforced via strict Firestore rules, guaranteeing that read/write operations are strictly limited to your authenticated UID. <em>(Note: The Groq API key is currently utilized within the client-side extension context).</em></p>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">7. Contact Us</h2>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">For privacy concerns, please use our <a href="contact.html" style="color: var(--accent);">Contact Page</a> or refer to our <a href="cookie-policy.html" style="color: var(--accent);">Cookie Policy</a> for detailed cookie usage.</p>
        </div>
'''

# 3. Terms of Service
pages["terms.html"] = '''
        <div class="fade-up" style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
            <h1 style="font-size: 3rem; font-weight: 800; margin-bottom: 1rem;">Terms of <span style="color: var(--accent)">Service</span></h1>
            
            <h2 style="font-size: 1.5rem; margin-bottom: 1rem; margin-top: 2rem;">1. Acceptance of Terms</h2>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">By accessing or using AppliSync, you agree to be bound by these Terms. If you disagree with any part of these terms, you may not access our service.</p>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">2. Description of Service</h2>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">AppliSync provides a Chrome Extension that automatically captures job data, a web dashboard for pipeline management, and AI-powered metadata extraction to optimize your job hunt.</p>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">3. Eligibility & User Accounts</h2>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">You must be at least 13 years old (or 18 depending on your jurisdiction) to use AppliSync. User accounts are authenticated via Google, GitHub, or Email/Password through Firebase Auth. You are solely responsible for maintaining the security of your account credentials.</p>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">4. Acceptable Use</h2>
            <ul style="color: var(--text-secondary); margin-bottom: 2rem; padding-left: 1.5rem;">
                <li>Do not misuse, overload, or attempt to reverse-engineer the AI extraction engine.</li>
                <li>Do not use AppliSync to scrape mass data for commercial redistribution.</li>
                <li>Do not attempt to access or tamper with other users' Firestore documents.</li>
            </ul>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">5. Intellectual Property</h2>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">The AppliSync UI, code, and "Obsidian Velvet" design system are proprietary intellectual property. You may not copy or redistribute these assets without authorization.</p>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">6. Third-Party Services & Warranties</h2>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">AppliSync relies on Firebase, Groq, and FormSubmit. Their respective Terms of Service apply. AppliSync is provided "As-is". We make no warranties regarding 100% accuracy of the AI extraction engine.</p>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">7. Limitation of Liability & Termination</h2>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">AppliSync is not liable for missed job applications or lost opportunities due to DOM parsing failures or downtime. We reserve the right to terminate or suspend access to our service immediately, without prior notice or liability, for any violation of these Terms.</p>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">8. Changes & Governing Law</h2>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">We reserve the right to modify these terms at any time. Changes will be communicated via the dashboard or email. These terms are governed by the laws of India. For legal queries, visit our <a href="contact.html" style="color: var(--accent);">Contact Page</a>.</p>
        </div>
'''

# 4. Cookie Policy
pages["cookie-policy.html"] = '''
        <div class="fade-up" style="max-width: 800px; margin: 0 auto; line-height: 1.8;">
            <h1 style="font-size: 3rem; font-weight: 800; margin-bottom: 1rem;">Cookie <span style="color: var(--accent)">Policy</span></h1>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem; margin-top: 2rem;">1. What Are Cookies?</h2>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">Cookies and local storage mechanisms are small pieces of data stored on your device that help web applications remember state, maintain sessions, and function properly.</p>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">2. Storage Mechanisms AppliSync Uses</h2>
            
            <table style="width: 100%; border-collapse: collapse; margin-bottom: 2rem; color: var(--text-secondary); background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px; overflow: hidden;">
                <tr style="background: var(--bg-secondary); border-bottom: 1px solid var(--border);">
                    <th style="padding: 1rem; text-align: left;">Type / Key</th>
                    <th style="padding: 1rem; text-align: left;">Purpose</th>
                    <th style="padding: 1rem; text-align: left;">Duration</th>
                </tr>
                <tr style="border-bottom: 1px solid var(--border);">
                    <td style="padding: 1rem;"><strong>Firebase Auth</strong><br><small>firebase:authUser</small></td>
                    <td style="padding: 1rem;">Persists your secure login session across the platform.</td>
                    <td style="padding: 1rem;">Session / Until sign-out</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border);">
                    <td style="padding: 1rem;"><strong>Chrome Local Storage</strong><br><small>chrome.storage.local</small></td>
                    <td style="padding: 1rem;">Temporarily caches form inputs while you apply on job boards.</td>
                    <td style="padding: 1rem;">Until application is saved</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border);">
                    <td style="padding: 1rem;"><strong>Session Storage</strong><br><small>Auth Sync Token</small></td>
                    <td style="padding: 1rem;">Syncs identity between the extension and dashboard.</td>
                    <td style="padding: 1rem;">Session</td>
                </tr>
                <tr>
                    <td style="padding: 1rem;"><strong>FormSubmit</strong><br><small>Third-party Cookie</small></td>
                    <td style="padding: 1rem;">Required for secure contact form handling and spam prevention.</td>
                    <td style="padding: 1rem;">Short-lived</td>
                </tr>
            </table>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">3. What We Do NOT Use</h2>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">AppliSync <strong>does not</strong> use advertising tracking cookies or intrusive third-party marketing analytics cookies.</p>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">4. How to Manage Cookies</h2>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">
                You can clear your Chrome extension storage by navigating to <code>chrome://extensions/</code> → AppliSync → Details → Clear Storage.<br>
                For standard web cookies, you can clear them via your browser's history and security settings.
            </p>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">5. Third-Party & Updates</h2>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">Our backend providers (Firebase and Groq) may set their own essential cookies; refer to their policies for details. We will update this policy if our storage mechanisms change. Contact us via the <a href="contact.html" style="color: var(--accent);">Contact Page</a> for questions.</p>
        </div>
'''

# 5. Support
pages["support.html"] = '''
        <div class="fade-up" style="max-width: 1000px; margin: 0 auto; text-align: center;">
            <div style="display: inline-block; padding: 6px 16px; border-radius: 100px; background: rgba(52, 168, 83, 0.1); border: 1px solid rgba(52, 168, 83, 0.2); color: #34A853; font-weight: 700; font-size: 0.8rem; margin-bottom: 1rem;">
                ● All systems operational
            </div>
            
            <h1 style="font-size: 3rem; font-weight: 800; margin-bottom: 1rem;">AppliSync <span style="color: var(--accent)">Support</span></h1>
            <p style="color: var(--text-secondary); margin-bottom: 3rem;">How can we help you track better today?</p>
            
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 2rem; text-align: left; margin-bottom: 4rem;">
                <!-- Quick Help Cards -->
                <div style="padding: 2rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 16px; transition: transform 0.2s;">
                    <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;">🧩 Extension not detecting jobs?</h3>
                    <p style="color: var(--text-secondary); margin-bottom: 1rem; font-size: 0.9rem;">Check <code>chrome://extensions/</code>, ensure Developer Mode is ON, and Reload unpacked.</p>
                </div>
                <div style="padding: 2rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 16px;">
                    <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;">📊 Dashboard not loading?</h3>
                    <p style="color: var(--text-secondary); margin-bottom: 1rem; font-size: 0.9rem;">Try hard refreshing (Ctrl+F5) or verifying your local Python server is running on port 8000.</p>
                </div>
                <div style="padding: 2rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 16px;">
                    <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;">🔑 Login & Auth Issues</h3>
                    <p style="color: var(--text-secondary); margin-bottom: 1rem; font-size: 0.9rem;">Confirm you are logged in with the exact same account on both the extension and dashboard. The APPLISYNC_AUTH_SYNC message handles the bridge.</p>
                </div>
                <div style="padding: 2rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 16px;">
                    <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;">🤖 AI extraction giving wrong data?</h3>
                    <p style="color: var(--text-secondary); margin-bottom: 1rem; font-size: 0.9rem;">AI parses DOM text; accuracy depends on page structure. If an API error occurs, the Groq API key quota may be hit.</p>
                </div>
            </div>

            <div style="background: var(--bg-secondary); border: 1px solid var(--border); border-radius: 24px; padding: 3rem; text-align: left; margin-bottom: 3rem;">
                <h2 style="font-size: 1.8rem; margin-bottom: 1rem;">Supported Job Boards</h2>
                <p style="color: var(--text-secondary); margin-bottom: 1rem;">Currently, AppliSync's Auto-Pilot officially supports extraction from <strong>LinkedIn, Indeed, Glassdoor, Naukri, and Wellfound</strong>. We are actively expanding this list!</p>
            </div>

            <div>
                <a href="contact.html" class="btn-primary-lg" style="display: inline-block; margin-right: 1rem;">Contact Support Team</a>
                <a href="https://github.com/ShubhamV2503/Applli-Sync" target="_blank" class="btn-ghost" style="display: inline-block; padding: 14px 36px; border-radius: 10px; font-weight: 700;">Report Bug on GitHub</a>
            </div>
        </div>
'''

# 6. Documentation
pages["documentation.html"] = '''
        <div class="fade-up" style="max-width: 900px; margin: 0 auto; line-height: 1.8;">
            <h1 style="font-size: 3rem; font-weight: 800; margin-bottom: 1rem;">Technical <span style="color: var(--accent)">Documentation</span></h1>
            <p style="color: var(--text-secondary); margin-bottom: 3rem; font-size: 1.1rem;">AppliSync is an AI-powered tracker that bridges a background Chrome Extension with a Firebase-powered Web Dashboard via the Groq LLM API.</p>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">1. Tech Stack & Architecture</h2>
            <table style="width: 100%; border-collapse: collapse; margin-bottom: 2rem; color: var(--text-secondary); border: 1px solid var(--border); border-radius: 12px; overflow: hidden; background: var(--bg-card);">
                <tr style="border-bottom: 1px solid var(--border);"><td style="padding: 1rem; width: 30%;"><strong>Frontend Layer</strong></td><td style="padding: 1rem;">Vanilla HTML/CSS/JS, "Obsidian Velvet" Design System</td></tr>
                <tr style="border-bottom: 1px solid var(--border);"><td style="padding: 1rem;"><strong>Auth & Database</strong></td><td style="padding: 1rem;">Firebase Auth + Firestore (joyboy-b6f27)</td></tr>
                <tr><td style="padding: 1rem;"><strong>AI Engine</strong></td><td style="padding: 1rem;">Groq API (llama-3.3-70b-versatile)</td></tr>
            </table>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">2. Component Deep-Dives</h2>
            <ul style="color: var(--text-secondary); margin-bottom: 2rem; padding-left: 1.5rem;">
                <li><strong>Chrome Extension (Manifest V3):</strong> Uses <code>MutationObserver</code> for Auto-Pilot mode. Captures page text and form state.</li>
                <li><strong>Dashboard:</strong> A centralized Firebase portal. Listens for <code>window.postMessage</code> auth syncs from the extension.</li>
                <li><strong>Landing Pages:</strong> Fully static, SEO-optimized, utilizing serverless FormSubmit for contact inquiries.</li>
            </ul>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">3. Setup Guide</h2>
            <div style="background: var(--bg-secondary); padding: 1.5rem; border-radius: 12px; border: 1px solid var(--border); margin-bottom: 2rem;">
                <strong style="color: var(--text-primary);">Web Dev:</strong> <code>python -m http.server 8000</code><br><br>
                <strong style="color: var(--text-primary);">Extension Install:</strong><br>
                1. Go to <code>chrome://extensions</code><br>
                2. Enable Developer Mode<br>
                3. Click "Load Unpacked" and select the repository folder.
            </div>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">4. AI Extraction Output Schema</h2>
            <pre style="background: #1e293b; color: #cbd5e1; padding: 1.5rem; border-radius: 12px; overflow-x: auto; font-family: monospace; font-size: 0.9rem; margin-bottom: 2rem;">{
  "company_name": "",
  "job_title": "",
  "experience_required": "",
  "salary_range": "",
  "hr_intelligence": {
    "recruiter_name": "",
    "linkedin_profile": ""
  }
}</pre>

            <h2 style="font-size: 1.5rem; margin-bottom: 1rem;">5. Security & Extensibility</h2>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">
                <strong>Security:</strong> The Groq API key currently resides in <code>content.js</code>. For strict production, proxy this via Firebase Cloud Functions. Ensure Firestore rules validate the UID on write operations.<br>
                <strong>Extending:</strong> To add new job boards, simply update the System Prompt instruction set within the <code>extractJobDataViaAI</code> function inside `content.js`.
            </p>
        </div>
'''

# 7. FAQ
pages["faq.html"] = '''
        <div class="fade-up" style="max-width: 800px; margin: 0 auto;">
            <h1 style="font-size: 3rem; font-weight: 800; margin-bottom: 3rem; text-align: center;">Frequently Asked <span style="color: var(--accent)">Questions</span></h1>
            
            <h2 style="font-size: 1.2rem; color: var(--accent); margin-bottom: 1.5rem; text-transform: uppercase; letter-spacing: 1px;">General</h2>
            <div style="margin-bottom: 1.5rem; padding: 1.5rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px;">
                <h3 style="font-weight: 700; margin-bottom: 0.5rem;">What is AppliSync?</h3>
                <p style="color: var(--text-secondary);">AppliSync is an AI-powered platform that automatically tracks your job applications across various websites and visualizes them in a central dashboard.</p>
            </div>
            <div style="margin-bottom: 3rem; padding: 1.5rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px;">
                <h3 style="font-weight: 700; margin-bottom: 0.5rem;">Which browsers are supported?</h3>
                <p style="color: var(--text-secondary);">Currently, our background tracker exclusively supports Google Chrome (and Chromium-based browsers) utilizing Manifest V3.</p>
            </div>

            <h2 style="font-size: 1.2rem; color: var(--accent); margin-bottom: 1.5rem; text-transform: uppercase; letter-spacing: 1px;">Extension & AI</h2>
            <div style="margin-bottom: 1.5rem; padding: 1.5rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px;">
                <h3 style="font-weight: 700; margin-bottom: 0.5rem;">Which job boards does AppliSync support?</h3>
                <p style="color: var(--text-secondary);">LinkedIn, Indeed, Glassdoor, and Naukri. The AI is highly versatile and works on many direct company sites as well.</p>
            </div>
            <div style="margin-bottom: 1.5rem; padding: 1.5rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px;">
                <h3 style="font-weight: 700; margin-bottom: 0.5rem;">What does "Auto-Pilot Mode" do?</h3>
                <p style="color: var(--text-secondary);">It silently monitors the DOM. When you hit "Apply", it triggers the Groq AI to read the page structure and extract metadata without you lifting a finger.</p>
            </div>
            <div style="margin-bottom: 3rem; padding: 1.5rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px;">
                <h3 style="font-weight: 700; margin-bottom: 0.5rem;">Does it store my job board login credentials?</h3>
                <p style="color: var(--text-secondary);">No. AppliSync only reads the public job description text and the form fields you actively type into related to the job application.</p>
            </div>

            <h2 style="font-size: 1.2rem; color: var(--accent); margin-bottom: 1.5rem; text-transform: uppercase; letter-spacing: 1px;">Privacy & Technical</h2>
            <div style="margin-bottom: 1.5rem; padding: 1.5rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px;">
                <h3 style="font-weight: 700; margin-bottom: 0.5rem;">Where is my data stored?</h3>
                <p style="color: var(--text-secondary);">All persistent data is securely stored in Firebase Firestore, locked exclusively to your authenticated UID.</p>
            </div>
            <div style="margin-bottom: 1.5rem; padding: 1.5rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px;">
                <h3 style="font-weight: 700; margin-bottom: 0.5rem;">Is my data sent to an AI?</h3>
                <p style="color: var(--text-secondary);">Yes, the raw job posting text is transmitted to the Groq API (LLaMA 3.3) purely for parsing. We do not sell your data.</p>
            </div>
        </div>
'''

# 8. How It Works
pages["how-it-works.html"] = '''
        <div class="fade-up" style="text-align: center; max-width: 900px; margin: 0 auto;">
            <h1 style="font-size: 3.5rem; font-weight: 900; margin-bottom: 1rem; letter-spacing: -1px;">How It <span style="color: var(--accent);">Works</span></h1>
            <p style="color: var(--text-secondary); margin-bottom: 4rem; font-size: 1.2rem;">A seamless pipeline from application to offer.</p>
            
            <div style="display: flex; flex-direction: column; gap: 3rem; text-align: left;">
                
                <div style="display: flex; align-items: center; gap: 3rem; background: var(--bg-card); padding: 3rem; border: 1px solid var(--border); border-radius: 24px;">
                    <div style="flex: 1;">
                        <span style="font-size: 4rem; font-weight: 900; color: var(--border-light); line-height: 1;">01</span>
                        <h2 style="font-size: 2rem; color: var(--accent); margin-bottom: 1rem; margin-top: -2rem; position: relative;">Install the Extension</h2>
                        <p style="color: var(--text-secondary); font-size: 1.1rem; line-height: 1.7;">Download AppliSync from the Chrome Web Store (or load unpacked for developers). Sign in with Google, GitHub, or Email to securely link your browser to your dashboard.</p>
                    </div>
                </div>

                <div style="display: flex; align-items: center; gap: 3rem; background: var(--bg-card); padding: 3rem; border: 1px solid var(--border); border-radius: 24px;">
                    <div style="flex: 1;">
                        <span style="font-size: 4rem; font-weight: 900; color: var(--border-light); line-height: 1;">02</span>
                        <h2 style="font-size: 2rem; color: var(--accent); margin-bottom: 1rem; margin-top: -2rem; position: relative;">Browse Job Boards Normally</h2>
                        <p style="color: var(--text-secondary); font-size: 1.1rem; line-height: 1.7;">Visit LinkedIn, Indeed, Glassdoor, etc. AppliSync's Auto-Pilot Mode runs silently in the background, using a MutationObserver to intelligently watch for application flow events.</p>
                    </div>
                </div>

                <div style="display: flex; align-items: center; gap: 3rem; background: var(--bg-card); padding: 3rem; border: 1px solid var(--border); border-radius: 24px;">
                    <div style="flex: 1;">
                        <span style="font-size: 4rem; font-weight: 900; color: var(--border-light); line-height: 1;">03</span>
                        <h2 style="font-size: 2rem; color: var(--accent); margin-bottom: 1rem; margin-top: -2rem; position: relative;">AI Captures the Data</h2>
                        <p style="color: var(--text-secondary); font-size: 1.1rem; line-height: 1.7;">When you click apply, AppliSync packages the page content and sends it to the Groq AI engine (LLaMA 3.3). It extracts structured metadata: company name, job title, salary range, and even HR/recruiter intelligence.</p>
                    </div>
                </div>

                <div style="display: flex; align-items: center; gap: 3rem; background: var(--bg-card); padding: 3rem; border: 1px solid var(--border); border-radius: 24px;">
                    <div style="flex: 1;">
                        <span style="font-size: 4rem; font-weight: 900; color: var(--border-light); line-height: 1;">04</span>
                        <h2 style="font-size: 2rem; color: var(--accent); margin-bottom: 1rem; margin-top: -2rem; position: relative;">Data Syncs to Dashboard</h2>
                        <p style="color: var(--text-secondary); font-size: 1.1rem; line-height: 1.7;">The extracted data is saved to your personal Firebase Firestore document in real-time. No manual data entry or spreadsheets required—it just appears on your Intelligence Command Dashboard.</p>
                    </div>
                </div>

                <div style="display: flex; align-items: center; gap: 3rem; background: var(--bg-card); padding: 3rem; border: 1px solid var(--border); border-radius: 24px;">
                    <div style="flex: 1;">
                        <span style="font-size: 4rem; font-weight: 900; color: var(--border-light); line-height: 1;">05</span>
                        <h2 style="font-size: 2rem; color: var(--accent); margin-bottom: 1rem; margin-top: -2rem; position: relative;">Manage Your Pipeline</h2>
                        <p style="color: var(--text-secondary); font-size: 1.1rem; line-height: 1.7;">View, filter, and analyze all your applications in one place. Track stages from Applied to Interviewing to Offer, and discover which platforms yield the highest interview conversion rates.</p>
                    </div>
                </div>

            </div>
            
            <div style="margin-top: 4rem;">
                <button onclick="window.location.href='dashboard/index.html'" class="btn-primary-lg">Open Dashboard Now →</button>
            </div>
        </div>
'''

for filename, content in pages.items():
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(get_base_template(content))
    print(f"Injected detailed content into {filename}")
