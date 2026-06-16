def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
    
for robot in range(6):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


    # or

    def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for _ in range(6):
    move()
    jump()



#or


number_of_hurdleas = 6
while number_of_hurdleas > 0 :
    jump()
    number_of_hurdleas -= 1
    print(number_of_hurdleas)
    