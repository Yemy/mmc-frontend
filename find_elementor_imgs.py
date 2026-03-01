"""
find_elementor_imgs.py
======================
Elementor embeds background images in data-settings JSON like:
  data-settings="{&quot;background_image&quot;:{&quot;url&quot;:&quot;images/foo.png&quot;}}"

These are NOT css url() or src= attributes so they won't be caught by regex on 
standard attribute patterns. This script:
1. Finds all unique image paths referenced inside data-settings in the RENDERED html
2. Checks whether those images exist on disk
3. Shows what paths need to be fixed in the Django template
"""
import re, os

TEMPLATE = 'f:/code/web/MMC/frontend/templates/index.html'
DISK     = 'f:/code/web/MMC/frontend/static/images'

with open(TEMPLATE, 'r', encoding='utf-8') as f:
    html = f.read()

disk_imgs = set(os.listdir(DISK))

# Find image paths inside data-settings JSON (encoded and raw)
# They appear as: "url":"images/..." or url&quot;:&quot;images/...
patterns = [
    r'"url"\s*:\s*"(images/[^"]+)"',           # JSON in data-settings
    r'&quot;url&quot;\s*:\s*&quot;(images/[^&]+)&quot;',  # HTML-entity encoded
    r"'url'\s*:\s*'(images/[^']+)'",           # single-quoted
]

found = set()
for p in patterns:
    found.update(re.findall(p, html))

print(f"Images found in Elementor data-settings: {len(found)}")
for img in sorted(found):
    fname = img.split('/')[-1] if '/' in img else img
    status = 'OK' if fname in disk_imgs else '!! MISSING !!'
    print(f"  [{status}] {img}")

# Also scan for any remaining bare images/ not wrapped by static
leftover = re.findall(r'(?<!")\bimages/[^\s\'"&>]+', html)
leftover = [l for l in leftover if '{%' not in l]
print(f"\nOther bare images/ refs NOT in static tags: {len(leftover)}")
for l in leftover[:20]:
    print(f"  {l}")
