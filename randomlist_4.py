# Banker Roulette
# Description
# Figure out how to pick a random name from the list of friends.

import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#google sarch ...get random item from list in python

#option 1
print(random .choice(friends))

#option 2
random_index = random.randint(0 , 4)
print(friends[random_index])

