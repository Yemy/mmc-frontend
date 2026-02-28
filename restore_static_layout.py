import re

with open('f:/code/web/MMC/frontend/extracted_content.html', 'r', encoding='utf-8') as f:
    body = f.read()

# We know extract_template.py included '<div id="content" class="site-content">' at the very beginning
# Let's extract the inner part to avoid doubling it, because base.html already provides it
inner_match = re.search(r'<div id="content" class="site-content">(.*?)<footer class="footer-two">', body, re.DOTALL)
if inner_match:
    inner_body = inner_match.group(1)
else:
    # try just removing the top wrapper
    inner_match = re.search(r'<div id="content" class="site-content">\s*(.*)\s*</div>\s*$', body, re.DOTALL)
    if inner_match:
        inner_body = inner_match.group(1)
    else:
        inner_body = body

final_template = """{% extends 'base.html' %}
{% load static %}
{% block content %}
""" + inner_body + """
{% endblock %}
"""

with open('f:/code/web/MMC/frontend/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(final_template)

print('Restored templates/index.html with pristine exact static structure.')
