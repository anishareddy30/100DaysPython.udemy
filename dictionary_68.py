programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
   
   }
print(programming_dictionary["Bug"])

programming_dictionary["loop"] =  "The action of doing something over and over again."
print(programming_dictionary)


#clearing the existing dictionary

# programming_dictionary = {}
# print(programming_dictionary)

programming_dictionary["bug"] = "a moth in computer"
print(programming_dictionary)

for thing in programming_dictionary:
    print(thing)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])    