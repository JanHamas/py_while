"""
**Garbage collection** is the process by which a programming language's runtime system automatically frees up memory that is no longer in use by the program. This helps prevent memory leaks, which occur when memory that is no longer needed isn't released, potentially causing a program to consume more and more memory over time.
"""

"""
In Python, garbage collection is handled by an automated memory management system, which includes a **reference counting** mechanism and a **cyclic garbage collector**.
"""
### 1. Reference Counting
"""
Python tracks how many references (or pointers) exist for each object in memory. Every time a new reference to an object is created, the reference count of that object is increased. When a reference is removed, the count decreases. 
"""
"""When an object's reference count drops to zero (meaning no variables or structures reference it), Python automatically deletes the object from memory, freeing up space.
"""
"""**Example:**
```python
a = [1, 2, 3]
b = a  # Both 'a' and 'b' reference the same list
del a  # Removes one reference
del b  # Now the list has no references and can be garbage-collected
"""
"""### 2. Cyclic Garbage Collection
Sometimes, objects can refer to each other in a cycle, which means their reference count will never reach zero even if they’re no longer accessible from the main program. For example:
"""
"""
a = []
b = []
a.append(b)
b.append(a)

"""
"""In this case, `a` and `b` reference each other, so their reference counts will never drop to zero.

Python's **cyclic garbage collector** is designed to detect these types of cycles and clean them up. It periodically checks for groups of objects that are only accessible by each other and not by any other part of the program. When it finds such cycles, it deletes them to free up memory.
"""
### Why Garbage Collection Matters
"""
Automatic garbage collection:
- Helps prevent memory leaks.
- Reduces the need for manual memory management.
- Ensures efficient memory use without requiring complex code to track and delete objects manually.
"""
"""
In Python, the garbage collection process is mostly invisible to the developer, letting you focus more on writing code and less on memory management.
"""