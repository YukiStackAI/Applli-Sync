import os
import glob
import re

base_dir = r'c:\Users\Admin\Desktop\Product\Applli-Sync\Applli-Sync'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add Home before Features
    if '<a href="index.html">Home</a>' not in content:
        content = content.replace('<a href="#features">Features</a>', '<a href="index.html">Home</a>\n                <a href="#features">Features</a>')
        content = content.replace('<a href="index.html#features">Features</a>', '<a href="index.html">Home</a>\n                <a href="index.html#features">Features</a>')

    # Remove Careers
    content = re.sub(r'<a href="careers\.html">Careers</a>\s*', '', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print('Navigation links updated.')
