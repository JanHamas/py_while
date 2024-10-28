"""
This line is a common Python pattern used to control how parts of a script are run, depending on how the file is being used. Let’s break it down simply:

__name__: This is a special built-in variable in Python. It holds the name of the current module (or file) that’s being run.

'__main__': When a Python file is run directly (not imported as a module), Python sets the __name__ variable to '__main__'.

Purpose of the if statement:

if __name__ == '__main__': checks whether this file is being run directly or being imported into another file.
If the file is being run directly, __name__ will be '__main__', and the code inside this block (like calling main()) will execute.
If the file is imported as a module in another file, __name__ will not be '__main__', so the code inside this block won’t run.
Example:
If you have a file named example.py:

def main():
    print("Hello, this is the main function!")

if __name__ == '__main__':
    main()
If you run example.py directly, it will print:

Hello, this is the main function!
But if you import example.py into another script, the main() function won’t automatically run.

Why Use This?
This pattern is useful for making Python files reusable as both standalone scripts and importable modules without executing the main code when imported 
"""


if __name__ == '__main__':
    main()
