import re

with open('f:/code/web/MMC/frontend/index.html', 'r', encoding='utf-8') as f:
    source = f.read()

# 1. Extract Head
head_match = re.search(r'(<!DOCTYPE html>.*?</head>)', source, re.DOTALL)
head = head_match.group(1)

# Fix static paths in head
head = re.sub(r'href="(css/.*?)"', r'href="{% static \'\1\' %}"', head)
head = re.sub(r'href="(fonts/.*?)"', r'href="{% static \'\1\' %}"', head)
head = re.sub(r'src="(js/.*?)"', r'src="{% static \'\1\' %}"', head)
head = re.sub(r'src="(images/.*?)"', r'src="{% static \'\1\' %}"', head)
head = re.sub(r'url\(\'(fonts/.*?)\'\)', r'url(\'{% static \'\1\' %}\')', head)

# Add load static and dynamic title/logo
head = "{% load static %}\n" + head
head = re.sub(r'<title>.*?</title>', r'<title>{% block title %}{{ site_settings.name|default:"MMC - Charity & Nonprofit" }}{% endblock %}</title>', head)
head = re.sub(r'<link rel="icon" href="{% static \'images/logo\.jpeg\' %}"', r'<link rel="icon" href="{% if site_settings.logo %}{{ site_settings.logo.url }}{% else %}{% static \'images/logo.jpeg\' %}{% endif %}"', head)
head = re.sub(r'<link rel="apple-touch-icon" href="{% static \'images/logo\.jpeg\' %}">', r'<link rel="apple-touch-icon" href="{% if site_settings.logo %}{{ site_settings.logo.url }}{% else %}{% static \'images/logo.jpeg\' %}{% endif %}">', head)


# 2. Extract Body Top (up to <div id="content">)
body_top_match = re.search(r'(<body.*?)<div id="content"', source, re.DOTALL)
body_top = body_top_match.group(1)
body_top = re.sub(r'src="(images/.*?)"', r'src="{% static \'\1\' %}"', body_top)
# Dynamic logos in body top
body_top = re.sub(r'<img src="{% static \'images/logo\.jpeg\' %}" alt="(.*?)"', r'<img src="{% if site_settings.logo %}{{ site_settings.logo.url }}{% else %}{% static \'images/logo.jpeg\' %}{% endif %}" alt="\1"', body_top)


# Fix topbar contact info
body_top = body_top.replace('admin@mulumesfincharity.org', '{{ site_settings.email|default:"contact@mulumesfincharity.org" }}')
body_top = body_top.replace('+251 914 008 942', '{{ site_settings.phone_1|default:"+251 914 008 942" }}')

# Add django URLs for main navigation. Since it's a huge block, we'll do general replaces on hrefs.
body_top = re.sub(r'<a href="/" aria-label="dropdown menu".*?>Home</a>', r'<a href="{% url \'web:index\' %}" aria-label="dropdown menu">Home</a>', body_top)
body_top = re.sub(r'<a href="https://mulumesfincharity\.org/about-us/">About Us</a>', r'<a href="{% url \'web:about\' %}">About Us</a>', body_top)
body_top = re.sub(r'<a href="https://mulumesfincharity\.org/causes/">Causes</a>', r'<a href="{% url \'web:programs\' %}">Programs</a>', body_top)
body_top = re.sub(r'<a href="https://mulumesfincharity\.org/blog/">Blog</a>', r'<a href="{% url \'web:blog_list\' %}">Blog</a>', body_top)
body_top = re.sub(r'<a href="https://mulumesfincharity\.org/contact-us/">.*Contact Us.*</a>', r'<a href="{% url \'web:contact\' %}">Contact Us</a>', body_top)
body_top = re.sub(r'<a href="https://mulumesfincharity\.org/contact-us/".*?class="btn--primary".*?>Donate Now<i class="fa-solid fa-arrow-right"></i></a>', r'<a href="{% url \'web:contact\' %}" class="btn--primary">Donate Now<i class="fa-solid fa-arrow-right"></i></a>', body_top)


# 3. Extract Footer (from <footer class="footer-two">)
footer_match = re.search(r'(<footer class="footer-two">.*</html>)', source, re.DOTALL)
footer = footer_match.group(1)
footer = re.sub(r'src="(js/.*?)"', r'src="{% static \'\1\' %}"', footer)
footer = re.sub(r'src="(images/.*?)"', r'src="{% static \'\1\' %}"', footer)

# Add custom blocks
footer = footer.replace('</body>', '    {% block extra_js %}{% endblock %}\n</body>')

# Dynamic logos in footer
footer = re.sub(r'<img src="{% static \'images/logo\.jpeg\' %}" alt="(.*?)"', r'<img src="{% if site_settings.logo %}{{ site_settings.logo.url }}{% else %}{% static \'images/logo.jpeg\' %}{% endif %}" alt="\1"', footer)

# Footer dynamic content
footer = footer.replace('admin@mulumesfincharity.org', '{{ site_settings.email|default:"contact@mulumesfincharity.org" }}')
footer = footer.replace('455 West Orchard Street Kings Mountain, NC 280867', '{{ site_settings.address|default:"Mekelle, Ethiopia" }}')

# Footer quick links
footer = footer.replace('href="https://mulumesfincharity.org/"', 'href="{% url \'web:index\' %}"')
footer = footer.replace('href="https://mulumesfincharity.org/blog/"', 'href="{% url \'web:blog_list\' %}"')


# 4. Construct base.html
base_content = f"""{head}
{body_top}
        <div id="content" class="site-content">
            {{% block content %}}{{% endblock %}}
        </div>
{footer}
"""

with open('f:/code/web/MMC/frontend/templates/base.html', 'w', encoding='utf-8') as f:
    f.write(base_content)

print("Base wrapper successfully built")
