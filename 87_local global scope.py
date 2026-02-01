""" Local Scope (Python)
Meaning

A local variable is created inside a function and can be used only inside that function."""

def my_function():
    x = 20
    print(x)

my_function()    

"""Global Scope (Python)
Meaning

A global variable is created outside all functions and can be used anywhere in the program."""

y = 20
def my_function():
    print(y)

my_function()    