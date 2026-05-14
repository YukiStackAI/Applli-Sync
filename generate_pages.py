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

# Base template
base_template = f"""<!DOCTYPE html>
<html lang="en">
{head}
<body>
    {nav}

    <!-- ═══ Main Content ═══ -->
    <main style="padding: 120px 2rem 80px; min-height: 80vh; max-width: 1200px; margin: 0 auto;">
        {{content}}
    </main>

    {footer}
</body>
</html>
"""

pages = {
    "contact.html": '''
        <div class="fade-up" style="max-width: 600px; margin: 0 auto; background: var(--bg-card); padding: 3rem; border-radius: 24px; border: 1px solid var(--border); box-shadow: 0 12px 24px rgba(0,0,0,0.05);">
            <h1 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 1rem;">Contact <span style="color: var(--accent)">Us</span></h1>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">Have questions about your tracking dashboard or need help? Send us a message.</p>
            <form onsubmit="event.preventDefault(); alert('Message sent successfully!');">
                <input type="text" class="auth-input" placeholder="Your Name" required>
                <input type="email" class="auth-input" placeholder="Your Email" required>
                <input type="text" class="auth-input" placeholder="Subject" required>
                <textarea class="auth-input" placeholder="Your Message" rows="5" style="resize: vertical;" required></textarea>
                <button type="submit" class="btn-primary-lg" style="width: 100%; margin-top: 1rem;">Send Message</button>
            </form>
        </div>
    ''',
    "privacy-policy.html": '''
        <div class="fade-up">
            <h1 style="font-size: 3rem; font-weight: 800; margin-bottom: 2rem;">Privacy Policy</h1>
            <div style="color: var(--text-secondary); line-height: 1.8;">
                <p>Last updated: April 2026</p><br>
                <h3 style="color: var(--text-primary); margin-bottom: 1rem; font-size: 1.5rem;">1. Information We Collect</h3>
                <p>AppliSync collects information you provide directly to us when using our platform or Chrome Extension. This includes your email, name, and job application metadata (such as job titles, company names, and dates applied).</p><br>
                <h3 style="color: var(--text-primary); margin-bottom: 1rem; font-size: 1.5rem;">2. How We Use Your Information</h3>
                <p>We use the information we collect to provide, maintain, and improve our services, including providing you with analytics about your job hunt and syncing data across your devices.</p><br>
                <h3 style="color: var(--text-primary); margin-bottom: 1rem; font-size: 1.5rem;">3. Data Security</h3>
                <p>We implement enterprise-grade security measures on Firebase Cloud to protect your personal information.</p>
            </div>
        </div>
    ''',
    "terms.html": '''
        <div class="fade-up">
            <h1 style="font-size: 3rem; font-weight: 800; margin-bottom: 2rem;">Terms of Service</h1>
            <div style="color: var(--text-secondary); line-height: 1.8;">
                <p>By accessing or using AppliSync, you agree to be bound by these Terms. If you disagree with any part of the terms, you may not access the service.</p><br>
                <h3 style="color: var(--text-primary); margin-bottom: 1rem; font-size: 1.5rem;">Acceptable Use</h3>
                <p>You agree not to use the service for any unlawful purpose or to violate any laws in your jurisdiction.</p><br>
                <h3 style="color: var(--text-primary); margin-bottom: 1rem; font-size: 1.5rem;">Account Responsibilities</h3>
                <p>You are responsible for safeguarding the password that you use to access the service and for any activities or actions under your password.</p>
            </div>
        </div>
    ''',
    "cookie-policy.html": '''
        <div class="fade-up">
            <h1 style="font-size: 3rem; font-weight: 800; margin-bottom: 2rem;">Cookie Policy</h1>
            <div style="color: var(--text-secondary); line-height: 1.8;">
                <p>We use cookies and similar tracking technologies to track the activity on our Service and hold certain information.</p><br>
                <h3 style="color: var(--text-primary); margin-bottom: 1rem; font-size: 1.5rem;">What are Cookies?</h3>
                <p>Cookies are files with a small amount of data which may include an anonymous unique identifier. They are sent to your browser from a website and stored on your device.</p>
            </div>
        </div>
    ''',
    "support.html": '''
        <div class="fade-up" style="text-align: center;">
            <h1 style="font-size: 3rem; font-weight: 800; margin-bottom: 1rem;">How can we <span style="color: var(--accent)">help?</span></h1>
            <p style="color: var(--text-secondary); margin-bottom: 3rem;">Search our knowledge base or browse categories below.</p>
            
            <input type="text" class="auth-input" placeholder="Search for help..." style="max-width: 500px; margin: 0 auto 3rem; padding: 1rem; font-size: 1.1rem; border-radius: 100px;">
            
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; text-align: left;">
                <div style="padding: 2rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 16px;">
                    <h3 style="font-size: 1.2rem; margin-bottom: 1rem;">Account Setup</h3>
                    <p style="color: var(--text-secondary);">Manage your profile, login issues, and security settings.</p>
                </div>
                <div style="padding: 2rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 16px;">
                    <h3 style="font-size: 1.2rem; margin-bottom: 1rem;">Extension Sync</h3>
                    <p style="color: var(--text-secondary);">Troubleshoot Chrome extension tracking and data capture.</p>
                </div>
                <div style="padding: 2rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 16px;">
                    <h3 style="font-size: 1.2rem; margin-bottom: 1rem;">Billing</h3>
                    <p style="color: var(--text-secondary);">Manage subscriptions, view invoices, and upgrade plans.</p>
                </div>
            </div>
        </div>
    ''',
    "documentation.html": '''
        <div class="fade-up">
            <h1 style="font-size: 3rem; font-weight: 800; margin-bottom: 2rem;">Documentation</h1>
            <div style="display: flex; gap: 4rem;">
                <div style="flex: 1; max-width: 250px; color: var(--text-secondary);">
                    <ul style="list-style: none; line-height: 2;">
                        <li><b style="color: var(--text-primary)">Getting Started</b></li>
                        <li>Installation</li>
                        <li>Configuration</li>
                        <li style="margin-top: 1rem;"><b style="color: var(--text-primary)">Core Features</b></li>
                        <li>Auto-Tracking</li>
                        <li>Dashboard Analytics</li>
                    </ul>
                </div>
                <div style="flex: 3; color: var(--text-secondary); line-height: 1.8;">
                    <h2 style="color: var(--text-primary); margin-bottom: 1rem;">Getting Started with AppliSync</h2>
                    <p>AppliSync is designed to silently track your applications in the background as you browse job portals. Once installed, simply go about your normal job application process on LinkedIn or Indeed, and AppliSync will log the data.</p>
                    <br>
                    <h3 style="color: var(--text-primary); margin-bottom: 1rem;">Installation</h3>
                    <p>1. Go to `chrome://extensions`<br>2. Enable Developer Mode<br>3. Click "Load Unpacked" and select the AppliSync directory.</p>
                </div>
            </div>
        </div>
    ''',
    "faq.html": '''
        <div class="fade-up" style="max-width: 800px; margin: 0 auto;">
            <h1 style="font-size: 3rem; font-weight: 800; margin-bottom: 2rem; text-align: center;">Frequently Asked <span style="color: var(--accent)">Questions</span></h1>
            
            <div style="margin-bottom: 1.5rem; padding: 1.5rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px;">
                <h3 style="font-weight: 700; margin-bottom: 0.5rem; color: var(--text-primary);">Does the extension work on all job sites?</h3>
                <p style="color: var(--text-secondary);">Currently, we officially support LinkedIn, Indeed, Glassdoor, and Naukri. We are continuously adding support for more platforms.</p>
            </div>
            
            <div style="margin-bottom: 1.5rem; padding: 1.5rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px;">
                <h3 style="font-weight: 700; margin-bottom: 0.5rem; color: var(--text-primary);">Is my data private?</h3>
                <p style="color: var(--text-secondary);">Absolutely. Your application data is stored securely in Firebase and is only accessible by you via your authenticated account.</p>
            </div>
            
            <div style="margin-bottom: 1.5rem; padding: 1.5rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px;">
                <h3 style="font-weight: 700; margin-bottom: 0.5rem; color: var(--text-primary);">Can I manually add an application?</h3>
                <p style="color: var(--text-secondary);">Yes, you can manually add applications directly from the Intelligence Command Dashboard.</p>
            </div>
        </div>
    ''',
    "how-it-works.html": '''
        <div class="fade-up" style="text-align: center; max-width: 900px; margin: 0 auto;">
            <h1 style="font-size: 3rem; font-weight: 800; margin-bottom: 1rem;">How It <span style="color: var(--accent)">Works</span></h1>
            <p style="color: var(--text-secondary); margin-bottom: 4rem; font-size: 1.2rem;">A seamless pipeline from application to offer.</p>
            
            <div style="display: flex; flex-direction: column; gap: 4rem; text-align: left;">
                <div style="display: flex; align-items: center; gap: 3rem;">
                    <div style="flex: 1; padding: 3rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 24px;">
                        <h2 style="font-size: 2rem; color: var(--accent); margin-bottom: 1rem;">1. Apply Normally</h2>
                        <p style="color: var(--text-secondary);">Browse LinkedIn, Indeed, or company sites. When you click apply and submit your application, our extension silently captures the job details, role, and company name.</p>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 3rem; flex-direction: row-reverse;">
                    <div style="flex: 1; padding: 3rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 24px;">
                        <h2 style="font-size: 2rem; color: var(--accent); margin-bottom: 1rem;">2. Auto-Sync to Cloud</h2>
                        <p style="color: var(--text-secondary);">The extension immediately syncs the metadata to your secure Firebase database. No manual data entry or spreadsheets required.</p>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 3rem;">
                    <div style="flex: 1; padding: 3rem; background: var(--bg-card); border: 1px solid var(--border); border-radius: 24px;">
                        <h2 style="font-size: 2rem; color: var(--accent); margin-bottom: 1rem;">3. Track & Optimize</h2>
                        <p style="color: var(--text-secondary);">Open your Dashboard to view pipeline analytics. Move applications through stages (Applied -> Interviewing -> Offer) and discover which platforms yield the best results.</p>
                    </div>
                </div>
            </div>
        </div>
    '''
}

for filename, content in pages.items():
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(base_template.replace('{content}', content))
    print(f"Generated {filename}")
