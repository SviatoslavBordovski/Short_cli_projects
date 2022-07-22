import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

def generate_data_list():
  """Generate data depending on user's input in command prompt"""
  data_list = list()

  # Choosing number of letters that user wants and make a random string with join function
  letter = ""
  for ch_letters in range(1, nr_letters + 1):
    letter += random.choice(letters)

  data_list.append(letter)

  # Choosing number of symbols from the list that user wants and make a random string with join
  symbol = ""
  for ch_symbols in range(1, nr_symbols + 1):
    symbol += random.choice(symbols)

  data_list.append(symbol)

  # Choosing numbers that user passed and make a random string with join function
  number = ""
  for ch_numbers in range(1, nr_numbers + 1):
    number += random.choice(numbers)

  data_list.append(number)

  print(data_list)
  return data_list


def create_strong_password():
  """Generate string from the list and reorder the list randomly"""
  random_data_list = generate_data_list()

  # Generated string using list of letters, numbers and symbols
  generated_string = ''.join(random.sample(random_data_list, len(random_data_list)))
  
  # Reorder string randomly
  final_pwd = ''.join(random.sample(generated_string, len(generated_string)))
  
  print("Generated password: ", final_pwd)


# Invoke magic password generator
create_strong_password()
