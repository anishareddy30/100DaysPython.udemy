# For Loops with Range
# Description
# The combination of the range() function with the Python For Loop allows us to run a loop
# for as many times as we wish. Instead of looping through each item in a List, 
# we can loop through a range of numbers.
# Range Function
# range(1, 10)

for number in range(1 , 11 , 2):
    print(number)

#adding no from 1 to 100
initial = 0
for number in range(1 , 101) :
    initial += number
print(initial)       