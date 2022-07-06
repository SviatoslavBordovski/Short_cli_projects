print("Welcome to Python Pizza Delivery!")

size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
  print("Small Pizza: $15")
  bill += 15
elif size == "M":
  print("Medium Pizza: $20")
  bill += 20
elif size == "L":
  print("Large Pizza: $25")
  bill += 25
  
if add_pepperoni == "Y":
  if size == "S":
    print("Pepperoni for Small Pizza: +$2")
    bill += 2
  else:
    print("Pepperoni for Medium or Large Pizza: +$3")
    bill += 3

if extra_cheese == "Y":
  print("Extra cheese for any size pizza: + $1")
  bill += 1

print(f"Your final bill is: ${bill}.")
