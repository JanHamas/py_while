In Python, you can delete files using the `os` or `pathlib` library. Here’s how to do it in a simple way:

### 1. **Using `os.remove()`**

The `os` module provides the `remove()` method to delete a file by specifying its path.

```python
import os

file_path = "myfile.txt"

# Check if the file exists before deleting
if os.path.exists(file_path):
    os.remove(file_path)  # Delete the file
    print(f"{file_path} has been deleted.")
else:
    print(f"{file_path} does not exist.")
```

This code deletes `myfile.txt` if it exists.

### 2. **Using `pathlib.Path.unlink()`**

The `pathlib` module (available in Python 3.4+) offers a more object-oriented approach:

```python
from pathlib import Path

file_path = Path("myfile.txt")

# Check if the file exists before deleting
if file_path.exists():
    file_path.unlink()  # Delete the file
    print(f"{file_path} has been deleted.")
else:
    print(f"{file_path} does not exist.")
```

Here, `Path.unlink()` deletes `myfile.txt` if it exists.

### 3. **Deleting Multiple Files**

If you want to delete multiple files in a directory that match a pattern (e.g., all `.txt` files), you can combine `glob` with `os.remove()` or `Path.unlink()`.

Using `os`:

```python
import os
import glob

for file_path in glob.glob("*.txt"):  # Find all .txt files in the current directory
    os.remove(file_path)
    print(f"{file_path} has been deleted.")
```

Using `pathlib`:

```python
from pathlib import Path

for file_path in Path(".").glob("*.txt"):  # Find all .txt files in the current directory
    file_path.unlink()
    print(f"{file_path} has been deleted.")
```

### Summary

- **Single file**: Use `os.remove("filename")` or `Path("filename").unlink()`
- **Multiple files**: Use a loop with `glob` to delete files matching a pattern