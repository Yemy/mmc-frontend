"""
rebuild_index_template.py
=========================
Reads the original static index.html, extracts the content block,
converts ALL image/css/js paths to Django static tags exactly ONCE,
and writes the result to templates/index.html.

This replaces the old extract_template.py + fix_images.py + fix_double_static.py approach
with a single, clean, atomic operation.
"""

import re

SOURCE = 'f:/code/web/MMC/frontend/index.html'
OUTPUT = 'f:/code/web/MMC/frontend/templates/index.html'

with open(SOURCE, 'r', encoding='utf-8') as f:
    source = f.read()

# ── 1. Extract the body content between <div id="content"> and <footer>
match = re.search(
    r'<div id="content" class="site-content">(.*?)<footer class="footer-two">',
    source,
    re.DOTALL
)
if not match:
    raise RuntimeError("Could not find content block in index.html")

content = match.group(1)

# ── 2. Convert src="images/..." → src="{% static 'images/...' %}"
# (Only if not already wrapped)
def wrap_src(m):
    path = m.group(1)
    return f'src="{{% static \'{path}\' %}}"'

content = re.sub(r'src="(images/[^"]+)"', wrap_src, content)

# ── 3. Convert srcset="images/... Xw, images/..." paths
def wrap_srcset_path(m):
    path = m.group(1)
    return f"{{% static '{path}' %}}"

content = re.sub(r'(?<=["\s,])(images/[^\s"\']+)(?=\s+\d+[wx])', wrap_srcset_path, content)
# Also handle bare srcset values that start with images/
content = re.sub(r'srcset="(images/[^"]+)"', lambda m: f'srcset="{{% static \'{m.group(1)}\' %}}"', content)

# ── 4. Convert url('images/...') inside style attributes
# These look like style="background-image:url('images/foo.png')"
# We must produce:  url('{% static 'images/foo.png' %}')
# The tricky part: Django accepts url("{% static 'x' %}") but NOT url('{% static 'x' %}')
# because the inner single quotes confuse the parser.  Use double quotes outside.
def wrap_url_in_style(m):
    path = m.group(1)
    # Use double quotes around the url() to avoid Django quote conflicts
    return f'url("{{% static \'{path}\' %}}")'

# Match url('images/...') or url("images/...")
content = re.sub(r'url\s*\([\'"]?(images/[^\'")\s]+)[\'"]?\)', wrap_url_in_style, content)

# ── 5. Fix data-bg="images/..." (Elementor background attribute)
def wrap_data_bg(m):
    path = m.group(1)
    return f'data-bg="{{% static \'{path}\' %}}"'

content = re.sub(r'data-bg="(images/[^"]+)"', wrap_data_bg, content)

# ── 6. Fix href links to known pages
content = content.replace('href="https://mulumesfincharity.org/causes/"',
                           "href=\"{% url 'web:programs' %}\"")
content = content.replace('href="https://mulumesfincharity.org/contact-us/"',
                           "href=\"{% url 'web:contact' %}\"")

# ── 7. Assemble the final Django template
final = (
    "{% extends 'base.html' %}\n"
    "{% load static %}\n"
    "\n"
    "{% block content %}\n"
    + content
    + "\n{% endblock %}\n"
)

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(final)

print(f"Written {len(final)} bytes to {OUTPUT}")
