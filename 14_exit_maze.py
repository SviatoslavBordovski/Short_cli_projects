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
        elif wall_in_front() and wall_on_right():
            turn_left()
        else:
            turn_right()
            
exit_maze()
