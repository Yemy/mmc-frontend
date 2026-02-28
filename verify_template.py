import os
import django
from django.test import RequestFactory

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmccore.settings')
django.setup()

from web.views import IndexView
request = RequestFactory().get('/')
try:
    response = IndexView.as_view()(request)
    response.render()
    print("SUCCESS: Homepage rendered with no errors!")
    print(f"Status: {response.status_code}")
    html = response.content.decode('utf-8')
    import re
    # Check for remaining unresolved image paths
    remaining = re.findall(r'(?:src|srcset|data-bg)\s*=\s*["\']images/', html)
    remaining += re.findall(r'url\(["\']?images/', html)
    print(f"Unmapped image paths remaining: {len(remaining)}")
    for r in remaining[:5]:
        print(' -', r)
except Exception as e:
    import traceback
    traceback.print_exc()
