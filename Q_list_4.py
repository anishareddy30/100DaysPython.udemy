#Given the code below:

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)
#What do you think will be printed?
# ans = replacing "Pears" with "Melons" and then appending "Lemons" to the end,


#Question 3:
#Given the code below:

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1])
#What will be printed?

# ans =
# Accessing elements using indexes
# dirty_dozen[0] → first list → fruits
# dirty_dozen[1] → second list → vegetables

# dirty_dozen[1][1]
# This means:
# Go to the second list ([1]) → the vegetables list.
# Then pick the second item ([1]) from that list.

# Similarly:
# dirty_dozen[0][1] refers to the second element in the fruits list, which is "Nectarines".