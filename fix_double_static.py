import re

with open('f:/code/web/MMC/frontend/templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# E.g. {% static '{% static 'images/banner-two-bg.png' %}' %}
text = re.sub(r'\{%\s*static\s+[\'"]\{%\s*static\s+[\'"](images/[^\'"]+)[\'"]\s*%}[\'"]\s*%}', r'{% static \'\1\' %}', text)

with open('f:/code/web/MMC/frontend/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

import urllib.request
try:
    with urllib.request.urlopen('http://127.0.0.1:8000/') as f:
        html = f.read().decode('utf-8')
    print('Homepage works!')
    matches = re.findall(r'"images/[^"]+"', html)
    matches += re.findall(r"'images/[^']+'", html)
    print(f'Found {len(matches)} "images/..." paths left over.')
except Exception as e:
    print('Failed:', e)
