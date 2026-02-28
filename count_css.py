import re
with open('f:/code/web/MMC/frontend/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'href=[\'\"]([^\'\"]+\.css)', text)
for m in matches:
    print(m.group(1))
