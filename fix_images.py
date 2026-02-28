import re

with open('f:/code/web/MMC/frontend/templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace any occurrence of images/... that is not already inside a {% static '...' %} tag
# We can use a regex with a negative lookbehind if possible, or just a simple function.
def replace_img(match):
    before = match.group(1)
    img_path = match.group(2)
    
    if "{% static" in before[-15:]:  # Rough check if we're already inside static
        return match.group(0)
    
    return f"{before}{{% static '{img_path}' %}}"

# We want to match things like `srcset="images/foo.png` or `src="images/foo.png` or `url(images/foo.png)`
text = re.sub(r'([\'"(, ]|\b)(images/[a-zA-Z0-9_\-./]+\.[a-zA-Z0-9]+)', replace_img, text)

with open('f:/code/web/MMC/frontend/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Images fixed!")
