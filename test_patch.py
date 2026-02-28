
import copy
from django.template import context

# Simulate the problem
class FakeBaseContext:
    def __init__(self):
        self.dicts = ["base"]
    
    def __copy__(self):
        # This simulates the Django 4.2 / Python 3.14 failure
        print("Executing broken __copy__...")
        duplicate = copy.copy(super())
        duplicate.dicts = self.dicts[:]
        return duplicate

# Patch logic
def fixed_copy(self):
    print("Executing fixed __copy__...")
    # Manually create the duplicate and copy the dicts
    cls = self.__class__
    duplicate = cls.__new__(cls)
    duplicate.__dict__.update(self.__dict__)
    duplicate.dicts = self.dicts[:]
    return duplicate

# Test without patch
print("--- Test 1: Broken Copy (expected failure) ---")
try:
    s = FakeBaseContext()
    copy.copy(s)
except AttributeError as e:
    print(f"Caught expected failure: {e}")

# Apply patch to FakeBaseContext
FakeBaseContext.__copy__ = fixed_copy

print("\n--- Test 2: Fixed Copy (expected success) ---")
s = FakeBaseContext()
c = copy.copy(s)
print(f"Copy successful! New object dicts: {c.dicts}")
print(f"Object type: {type(c)}")
print(f"Is new object: {c is not s}")
