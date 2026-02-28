import urllib.request
import re

try:
    with urllib.request.urlopen('http://127.0.0.1:8000/') as f:
        html = f.read().decode('utf-8')
        
    matches = re.findall(r'"images/[^"]+"', html)
    matches += re.findall(r"'images/[^']+'", html)
    print(f"Found {len(matches)} 'images/...' paths that might lack /static/.")
    for m in set(matches[:15]):
        print(m)
        
    css_matches = re.findall(r'"[^"]+\.css"', html)
    bad_css = [c for c in css_matches if '/static/' not in c and 'http' not in c]
    print(f"Found {len(bad_css)} bad css paths.")
    for c in set(bad_css[:10]):
        print(c)
except Exception as e:
    print('Failed to load:', e)
