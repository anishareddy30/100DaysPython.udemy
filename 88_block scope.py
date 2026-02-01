# Python does not have block scope.
# Variables inside if/for/while can be used outside, but variables inside functions cannot.

if True:
    x = 5

print(x)

# Even though x was inside if, Python allows it outside.

def my_func():
    y = 10
my_func    

# print(y) ❌ Error
# Variables inside a function cannot be used outside.
