with open('f:/code/web/MMC/frontend/templates/base.html', 'r', encoding='utf-8') as f:
    template = f.read()

template = template.replace("\\'", "'")
template = template.replace('\\"', '"')

with open('f:/code/web/MMC/frontend/templates/base.html', 'w', encoding='utf-8') as out:
    out.write(template)
print('Escaped quotes fixed in base.html')
