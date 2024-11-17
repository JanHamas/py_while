# In Python, `__all__` is a special list used in a module to specify which names (functions, classes, or variables) should be imported when someone uses:

from numpy import *
### Example:
# **Without `__all__`:**
# module.py
def func1():
    return "This is func1"

def func2():
    return "This is func2"

# Import everything
from module import *
print(func1())  # Works
print(func2())  # Works
```

**With `__all__`:**
```python
# module.py
__all__ = ['func1']  # Only func1 is accessible when importing with *

def func1():
    return "This is func1"

def func2():
    return "This is func2"

# Import everything
from module import *
print(func1())  # Works
print(func2())  # Error: NameError
```

### Why Use It?
- To control what gets imported with `*`.
- Helps avoid exposing internal helper functions or variables unintentionally.