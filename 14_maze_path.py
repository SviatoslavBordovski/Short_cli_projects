def turn_right():
    turn_left()
    turn_left()
    turn_left()

def find_a_flag():
    while not at_goal():
        while front_is_clear():
            move()
            if at_goal():
                break
            elif right_is_clear():
                turn_right()

        if front_is_clear() and right_is_clear():
            turn_right()
        elif wall_on_right() and wall_in_front():
            turn_left()
        elif right_is_clear() and wall_in_front():
            turn_right()
        elif right_is_clear() or wall_in_front():
            turn_right()

        else:
           break
            
find_a_flag()
