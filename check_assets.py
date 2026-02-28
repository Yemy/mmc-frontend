import re

with open('f:/code/web/MMC/frontend/rendered.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check for inline styles with url('images/...')
print('--- Unmapped url(images/...) ---')
for m in re.findall(r'url\s*\(\s*[\'\"]?(images/[^\'\"]+)[\'\"]?\s*\)', html):
    print(m)

# Check for src or srcset with images/...
print('--- Unmapped src=images/ ---')
for m in re.findall(r'(?:src|srcset)\s*=\s*[\'\"]([^\'\"]*images/[^\'\"]+)[\'\"]', html):
    # Only print if it doesn't clearly start with /static/
    if not m.startswith('/static/'):
        print(m[:100])

# Check for css
print('--- Unmapped css/ ---')
for m in re.findall(r'href\s*=\s*[\'\"](css/[^\'\"]+)[\'\"]', html):
    if not m.startswith('/static/'):
        print(m)

# Check for js
print('--- Unmapped js/ ---')
for m in re.findall(r'src\s*=\s*[\'\"](js/[^\'\"]+)[\'\"]', html):
    if not m.startswith('/static/'):
        print(m)
