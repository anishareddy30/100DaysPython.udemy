def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice?")
greet()


def greet_with_name(name):
    print(f"Hello{name}")
    print(f"How do you do?{name}")
greet_with_name("anisha")    

#here "name" is parameter and "anisha" is argument

#  Now the argument is the actual piece of data that's going to be passed over to this function when it's
# being called, whereas the parameter is the name of that data,

# and we use the parameter inside the function to refer to it and to do things with it.the parameter is the name of the data that's being passed in,
# the argument is the actual value of the data.