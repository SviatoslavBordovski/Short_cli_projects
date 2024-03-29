# Program that automatically prints the solution to the FizzBuzz game.
# It should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# Example output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz

num = 0

for num in range(1, 101):

  if num % 3 == 0 and num % 5 == 0:  # returns True (boolean)
    print("FizzBuzz")
  elif num % 3 == 0:  # returns True (boolean)
    print("Fizz")
  elif num % 5 == 0:  # returns True (boolean)
    print("Buzz")
  else:
    print(num)
