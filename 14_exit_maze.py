# Reborg 'Maze' task => https://bit.ly/37U18lU

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def exit_maze():
    while not at_goal():
        if front_is_clear():
            move()
            if right_is_clear():
                turn_right()
            else:
                turn_left()
                
             
        elif wall_in_front() and wall_on_right():
            turn_left()
        else:
            turn_right()
            move()

exit_maze()


# 2nd solution:

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def find_a_flag():
    while not at_goal():
        if right_is_clear() and not front_is_clear():
            turn_right()
            move()
        
        elif front_is_clear():
            move()
        else:
            turn_left()

find_a_flag()
