
# In Python, a decorator is a design pattern that allows you to modify or extend the behavior of a function or method without permanently changing its code. Decorators are commonly used to add functionality to functions, such as logging, access control, or timing the execution of a function.

# How Decorators Work
# A decorator is a function that takes another function as an argument, adds some functionality to it, and then returns a new function that includes the added functionality. In Python, decorators are often applied using the @decorator_name syntax above the function you want to decorate.

# Basic Example of a Decorator
# Here’s an example of a simple decorator that logs the execution of a function:

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# vbnet
# Copy code
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# Explanation:
# The my_decorator function is the decorator. It takes a function (func) as input and defines a nested function wrapper that adds functionality before and after calling func.
# When @my_decorator is placed above say_hello, it applies the decorator to say_hello, making say_hello execute with the added behavior.
# Common Use Cases of Decorators
# Logging – Record when functions start and end.
# Access Control/Authorization – Verify user permissions before executing functions.
# Memoization/Caching – Cache function results to improve performance.
# Timing – Measure the time a function takes to execute.
# Decorators with Arguments
# Decorators can also take arguments, which can allow for flexible behavior in reusable decorator code.

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
# Output:
# Copy code
# Hello, Alice
# Hello, Alice
# Hello, Alice
# In this example, repeat is a decorator that repeats the execution of greet a specified number of times.