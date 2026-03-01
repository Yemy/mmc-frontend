"""
patch_image_paths.py
====================
Finds ALL remaining bare 'images/...' paths in templates/index.html that are
still NOT wrapped in a {% static %} tag (e.g. inside JavaScript, data-* attrs,
srcset trailing paths after a space, etc.) and fixes them.

Also fixes any references in base.html.
"""
import re, os

IMAGE_DIR = 'f:/code/web/MMC/frontend/static/images'
TEMPLATE   = 'f:/code/web/MMC/frontend/templates/index.html'
BASE       = 'f:/code/web/MMC/frontend/templates/base.html'

disk_images = set(os.listdir(IMAGE_DIR))

def process(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    original = text

    # ── Pattern 1: href or src with bare images/ path not already in static tag
    def fix_attr(m):
        attr, q, val = m.group(1), m.group(2), m.group(3)
        if '{%' in val:   # already wrapped
            return m.group(0)
        return f'{attr}={q}{{% static \'{val}\' %}}{q}'

    text = re.sub(r'((?:src|href|data-bg|poster))\s*=\s*(["\'])(images/[^\2]+?)\2',
                  fix_attr, text)

    # ── Pattern 2: url('images/...') or url("images/...") not already wrapped
    def fix_url(m):
        path = m.group(1)
        if '{%' in path:
            return m.group(0)
        return f'url("{{% static \'{path}\' %}}")'

    text = re.sub(r'url\s*\(\s*["\']?(images/[^\'"\)]+)["\']?\s*\)', fix_url, text)

    # ── Pattern 3: bare images/... inside srcset (space-separated list)
    def fix_srcset_token(m):
        path = m.group(0)
        if '{%' in path:
            return path
        return f'{{% static \'{path}\' %}}'

    text = re.sub(r'\b(images/[^\s"\'>,\]]+)', fix_srcset_token, text)

    # ── Pattern 4: fix double-wrapped static (from any previous run)
    text = re.sub(
        r'\{%\s*static\s*[\'"]\{%\s*static\s*[\'"](images/[^\'"]+)[\'"]\s*%}[\'"]\s*%}',
        r"{% static '\1' %}",
        text
    )

    changed = text != original
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

    # Report bare leftovers
    remaining = re.findall(r'(?<![\'"])\bimages/\S+', text)
    remaining = [r for r in remaining if '{%' not in r]
    print(f"{'CHANGED' if changed else 'no change'}: {path}")
    print(f"  Remaining bare paths: {len(remaining)}")
    for r in remaining[:10]:
        print(f"    {r}")

process(TEMPLATE)
process(BASE)
