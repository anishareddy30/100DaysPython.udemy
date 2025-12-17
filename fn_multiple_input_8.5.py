# Functions with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
    
greet_with("Jack Bauer","Nowhere")

greet_with(name="Angela", location="London")
greet_with(location="London", name="Angela")

# Positional vs Keyword Arguments
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
