def greet_with_multiple_input (name , location):
    print(f"hello {name}")
    print(f"what is it like in {location}")

greet_with_multiple_input("anisha" , "india")    

greet_with_multiple_input(name = "anisha" , location = "india")
greet_with_multiple_input(location = "india" , name = "anisha")


# Positional vs Keyword Argument
# Description
# Multiple Inputs
# You can have multiple inputs in functions. All you need to do is separate them with a comma
# PAUSE 1
# Create a function with multiple inputs
# Hint >
# Positional Arguments
# By default, when you create a function in Python, it will keep the order of arguments in the function definition.
# e.g. In the function below, the first argument that goes in will always be printed before the second one.
# a = 2
# b = 1