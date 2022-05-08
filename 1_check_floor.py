# dash just comments out everything after in line that should be not executed by Python

inp = input ('Europe Floor?') # if user selected it, we just count starting from zero
usf = int(inp) + 1 # if user have chosen US floor, we convert it to an integer number (previous "inp") and make +1 as it is expected in US
print ('US floor', usf) # result of the US floor chosen

# Here is how for the user it looks like:
# Europe floor? 0
# US floor 1
