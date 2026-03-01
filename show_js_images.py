"""Show the context around the first 5 bare image/ references"""
import re

with open('f:/code/web/MMC/frontend/templates/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

found = 0
for i, line in enumerate(lines):
    if re.search(r'\bimages/[^\s"\'&>]+', line) and '{%' not in line:
        start = max(0, i - 3)
        end = min(len(lines), i + 3)
        print(f"--- Line {i+1} ---")
        print(''.join(lines[start:end]))
        found += 1
        if found >= 6:
            break
