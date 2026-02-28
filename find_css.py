import re
with open('f:/code/web/MMC/frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '.css' in line:
        print(f"Line {i+1}: {line.strip()[:150]}")
