
import copy

class Base:
    def __init__(self):
        self.dicts = ["base"]

class Sub(Base):
    def __init__(self):
        super().__init__()
        self.dicts = ["sub"]
    
    def __copy__(self):
        print("Screaming in 3.14...")
        try:
            # This is what Django does in Context.__copy__
            duplicate = copy.copy(super())
            print(f"Copy of super() returned type: {type(duplicate)}")
            duplicate.dicts = self.dicts[:]
            return duplicate
        except AttributeError as e:
            print(f"Caught expected AttributeError: {e}")
            return None

s = Sub()
copy.copy(s)
