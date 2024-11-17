# In Python, `*args` and `**kwargs` are used in function definitions to allow you to pass a variable number of arguments to a function.

### 1. `*args` (Non-Keyword Arguments)
'''
"Non-keyword arguments" (or positional arguments) are arguments passed to a function without specifying a keyword (or name) for each one. Instead, these arguments are identified by their position in the function call.
'''
# - `*args` lets you pass a variable number of *positional* arguments to a function.
''' 
In Python, positional refers to the order in which arguments are passed to a function. The number of positional arguments means the number of arguments that are passed without specifying their names and are instead assigned based on their position.
''' 
# - It gathers extra positional arguments into a tuple.
'''
**Example:**
def my_function(*args):
    for arg in args:
        print(arg)
my_function(1, 2, 3)  # This will print each number on a new line
'''

'''
**Output:**
1
2
3
'''

### 2. `**kwargs` (Keyword Arguments)
'''
- `**kwargs` lets you pass a variable number of *keyword* arguments (like a dictionary) to a function.
- It gathers extra keyword arguments into a dictionary.'''
'''
**Example:**
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(name="Alice", age=25, city="New York")
'''
'''
**Output:**
name: Alice
age: 25
city: New York
'''

### Using Both Together
'''
- You can use both `*args` and `**kwargs` in the same function to accept all types of extra arguments.
'''
'''
**Example:**
def my_function(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

my_function(1, 2, 3, name="Alice", age=25)
'''
'''
**Output:**
args: (1, 2, 3)
kwargs: {'name': 'Alice', 'age': 25}
'''

''' 
Summary
- `*args` is for a variable number of positional arguments.
- `**kwargs` is for a variable number of keyword arguments.
'''