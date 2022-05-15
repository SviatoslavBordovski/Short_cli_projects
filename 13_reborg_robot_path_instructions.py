# Reborg 'Hardle 4' task => https://bit.ly/3FOATcZ

# 1st solution:

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    while wall_on_right():
        move()
        if right_is_clear():
            turn_right()
            move()
            turn_right()
            break
        elif wall_in_front():
            turn_left()
        elif at_goal():
            break

def find_a_flag():
    while not at_goal():
        if front_is_clear():
            move()
        elif wall_on_right() and wall_in_front():
            turn_left()
            if wall_in_front():
                turn_left()
            jump()
        elif wall_in_front() or front_is_clear() and right_is_clear():
            turn_right()

find_a_flag()

# /------------------------------------------------------------------------/

# 2nd solution:

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

def find_a_flag():
    while not at_goal():
        if wall_in_front():
            jump()
        else:
            move()

find_a_flag()
