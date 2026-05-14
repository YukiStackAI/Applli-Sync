import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

head_match = re.search(r'(<head>.*?</head>)', html, re.DOTALL)
head = head_match.group(1) if head_match else '<head><title>AppliSync</title></head>'

nav_match = re.search(r'(<!-- ═══ Navbar ═══ -->.*?)</nav>', html, re.DOTALL)
nav = nav_match.group(1) + '</nav>' if nav_match else ''

footer_match = re.search(r'(<!-- ═══ Footer ═══ -->.*?)</body>', html, re.DOTALL)
footer = footer_match.group(1) if footer_match else '</footer>'

success_content = """
        <div class="fade-up" style="max-width: 600px; margin: 0 auto; background: var(--bg-card); padding: 4rem 3rem; border-radius: 24px; border: 1px solid var(--border); box-shadow: 0 12px 24px rgba(0,0,0,0.05); text-align: center;">
            <div style="width: 80px; height: 80px; background: rgba(52, 168, 83, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 2rem;">
                <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#34A853" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
            </div>
            <h1 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 1rem; color: var(--text-primary);">Message <span style="color: #34A853;">Sent</span>!</h1>
            <p style="color: var(--text-secondary); margin-bottom: 2.5rem; font-size: 1.1rem; line-height: 1.6;">Thank you for reaching out! The details have been sent successfully. Our team will get back to you shortly.</p>
            <button onclick="window.location.href='index.html'" class="btn-primary-lg" style="width: 100%;">Return to Home</button>
        </div>
"""

base_template = f"""<!DOCTYPE html>
<html lang="en">
{head}
<body>
    {nav}

    <!-- ═══ Main Content ═══ -->
    <main style="padding: 120px 2rem 80px; min-height: 80vh; max-width: 1200px; margin: 0 auto; display: flex; align-items: center; justify-content: center;">
        {success_content}
    </main>

    {footer}
</body>
</html>
"""

with open('success.html', 'w', encoding='utf-8') as f:
    f.write(base_template)

print("Generated success.html")
