import re

with open('f:/code/web/MMC/frontend/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<div class="row gutter-24 mt-4">.*?<div class="elementor-element elementor-element-bbfb9c9', text, re.DOTALL)
if m:
    print('Match length:', len(m.group(0)))
else:
    print('No match')
