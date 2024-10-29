# Python raise Keyword
'''
The raise keyword in Python is used to trigger exceptions intentionally.(ارادے کے ساتھ غلطی)This is useful to indicate that something went wrong or doesn’t meet specific conditions.
Basic Syntax
raise ExceptionType("Error message")
'''

'''
Raising a General Exception:
raise Exception("An error occurred")
Stops the program and displays: Exception: An error occurred.
'''

'''
Raising a Specific Exception:
Use specific exception types like ValueError, TypeError, etc., to indicate different error types.
x = -5
if x < 0:
    raise ValueError("x should be non-negative")
Raises a ValueError if x is negative.
'''

'''
Reraising an Exception:
Sometimes, you catch an exception but want to re-raise it to be handled elsewhere.
try:
    x = int("not a number")
except ValueError as e:
    print("Caught a ValueError:", e)
    raise  # Re-raises the caught exception

'''

''' 
Summary
Using raise helps enforce rules and handle unexpected cases, making code more robust and easier to debug.
'''