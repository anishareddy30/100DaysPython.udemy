# for item in list_of_items:
# #Do something to each item

# for number in range(a, b):
# print(number)

#while something_is_true_condn: ....it will continue the loop until condn is false
#Do something repeatedly

 def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# for step in range(6):  

number_of_hurdles = 6 
while number_of_hurdles > 0:
   jump()
   number_of_hurdles -= 1  #decresing value of 6 by 1 
   print(number_of_hurdles)

#this is the code for 6 hurdles in which bird is going to jump in half square format




#now below code is using loop coz we dont know the final ppoint so we need to put condn

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal(): #while our robot is not at the goal perform jump fn
   jump()

   #or

while at_goal() != True:
   jump()   


#INFINITE LOOP
while 5>3:
   jump()