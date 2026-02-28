import re

with open('f:/code/web/MMC/frontend/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract content between <div id="content" class="site-content"> and <footer class="footer-two">
match = re.search(r'(<div id="content" class="site-content">.+?)(?:<footer class="footer-two">)', html, re.DOTALL)
if match:
    content = match.group(1)
    
    # Process static files
    # Images (src="images/...")
    content = re.sub(r'src="images/(.*?)"', r'src="{% static \'images/\1\' %}"', content)
    # Background images (url('images/...'))
    content = re.sub(r'url\(\'images/(.*?)\'\)', r'url(\'{% static \'images/\1\' %}\')', content)
    
    with open('f:/code/web/MMC/frontend/extracted_content.html', 'w', encoding='utf-8') as out:
        out.write(content)
    print("Extraction successful")
else:
    print("Could not find content blocks")
