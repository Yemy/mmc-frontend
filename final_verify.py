
import os
import django
from django.conf import settings

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmccore.settings')
django.setup()

from django.template import Context
import copy

print("--- Final Verification ---")
try:
    ctx = Context({"test": "data"})
    print("Original context dicts:", ctx.dicts)
    
    # This crashed before the patch in Python 3.14
    ctx_copy = copy.copy(ctx)
    print("Copy successful!")
    print("Copied context dicts:", ctx_copy.dicts)
    print("Test passed: No AttributeError raised.")
except AttributeError as e:
    print(f"Test FAILED: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
