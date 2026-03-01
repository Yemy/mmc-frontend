"""Show context around bare image refs - check if they are in JS or HTML"""
import re

with open('f:/code/web/MMC/frontend/templates/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

found = 0
for i, line in enumerate(lines):
    # Find pattern: any 'images/something' NOT followed by %} (not already wrapped)
    if 'images/' in line and '{%' not in line:
        stripped = line.strip()[:180]
        print(f"Line {i+1}: {stripped}")
        found += 1
        if found >= 15:
            break
print(f"Total bare refs checked: {found}")
