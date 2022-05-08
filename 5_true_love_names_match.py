# Instructions in the module below

print("Welcome to the Love Calculator!")
man = input("What is his name? \n")
woman = input("What is her name? \n")

# man is Sviatoslav
# woman is Luidmyla

combined_names_string = man + woman
combined_names_string.lower()

t = combined_names_string.count("t")
r = combined_names_string.count("r")
u = combined_names_string.count("u")
e = combined_names_string.count("e")

match_for_true = t + r + u + e

l = combined_names_string.count("l")
o = combined_names_string.count("o")
v = combined_names_string.count("v")
e = combined_names_string.count("e")

match_for_love = l + o + v + e

final_match = str(match_for_true) + str(match_for_love)

if 10 > int(final_match) > 90:
  print("Your score is **x**, you go together like coke and mentos.")

elif 40 < int(final_match) < 50:
  print("Your score is **y**, you are alright together.")

else:
  print("Your score is **z**.")
  

# man = Sviatoslav
# woman = Luidmyla

# T occurs 1 times
# R occurs 0 times
# U occurs 1 time
# E occurs 0 times

# Total = 2

# L occurs 3 times
# O occurs 1 time
# V occurs 2 times
# E occurs 0 times

# Total = 5

# So Love Score = 25

# Test with names:
# man = Traversy
# woman = Lusia
