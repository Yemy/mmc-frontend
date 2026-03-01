"""
audit_images.py
Compares image refs in index.html vs what's available locally in images/
"""
import re, os

with open('f:/code/web/MMC/frontend/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# All image paths referenced in index.html
refs = set(re.findall(r'images/([^\s\'")\]>]+)', html))

# All image files on disk
disk = set(os.listdir('f:/code/web/MMC/frontend/images'))

print(f"Total image refs in index.html: {len(refs)}")
print(f"Total image files on disk: {len(disk)}")

missing = [r for r in sorted(refs) if r not in disk]
extra = [d for d in sorted(disk) if d not in refs and not d.endswith('.DS_Store')]

print(f"\n--- {len(missing)} REFERENCED but NOT ON DISK ---")
for m in missing:
    print(f"  images/{m}")

print(f"\n--- SAMPLE of {len(refs)} refs in index.html (first 30) ---")
for r in sorted(refs)[:30]:
    print(f"  {'OK' if r in disk else 'MISSING'}: images/{r}")
