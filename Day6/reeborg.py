def turn_around():
    turn_left()
    turn_left()
    
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

def move_up():
    turn_left()
    move()
    turn_right()

    
#What you need to know
# The functions move() and turn_left().
# The conditions front_is_clear() 
    # or wall_in_front(), at_goal(), 
        # and their negation.
# How to use a while loop and an if statement.




"""
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
"""

    
   

"""
number_of_hurtles = 6
position = True
while number_of_hurtles > 0:
    if position != at_goal():
        jump()
        number_of_hurtles -= 1
        print(number_of_hurtles)
    break;

# what we are supposed to do:
while not at_goal():
    jump()
"""
    
    
"""
number_of_hurtles = 6
while number_of_hurtles > 0:
    jump()
    number_of_hurtles -= 1
    print(number_of_hurtles)
"""
    
    

# Draw Square
"""
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
"""


# My play   
"""
turn_left()
move()
turn_right()
move()
turn_around()
turn_left()
move()
turn_left()
move()
"""





