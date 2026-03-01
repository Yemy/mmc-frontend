"""
check_rendered_imgs.py
Check rendered HTML for any image references that don't start with /static/
"""
import re

with open('f:/code/web/MMC/frontend/rendered.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all src / srcset / data-bg references
bare_src = []
for m in re.finditer(r'(?:src|srcset|data-bg|poster)\s*=\s*["\']([^"\']+)["\']', html):
    val = m.group(1)
    # Check individual srcset components
    for part in re.split(r',\s*', val):
        url = part.strip().split()[0]
        if url and not url.startswith('/static/') and not url.startswith('http') and not url.startswith('data:') and not url.startswith('//'):
            bare_src.append(url)

# Find url() references
for m in re.finditer(r'url\s*\(\s*["\']?([^"\')\s]+)["\']?\s*\)', html):
    val = m.group(1)
    if val and not val.startswith('/static/') and not val.startswith('http') and not val.startswith('data:') and not val.startswith('//') and not val.startswith('#'):
        bare_src.append(val)

print(f"Bare (non-static) image refs in rendered HTML: {len(bare_src)}")
for b in sorted(set(bare_src))[:30]:
    print(f"  {b}")
