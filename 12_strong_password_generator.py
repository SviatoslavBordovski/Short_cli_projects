import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

def generate_data_list():

  # Choosing number of letters that user wants and make a random string with join function
  ch_letters = str(''.join(random.sample(letters, nr_letters)))
  
  # Choosing numbers that user passed and make a random string with join function
  ch_numbers = str(''.join(random.sample(numbers, nr_numbers)))
  
  # Choosing number of symbols from the list that user wants and make a random string with join function
  ch_symbols = str(''.join(random.sample(symbols, nr_symbols)))
  
  data_list = [ch_letters, ch_numbers, ch_symbols]
  return data_list


def create_strong_password():
  random_data_list = generate_data_list()

  # Generated string using list of letters, numbers and symbols
  generated_string = ''.join(random.sample(random_data_list, len(random_data_list)))
  
  # Reorder string randomly
  final_pwd = ''.join(random.sample(generated_string, len(generated_string)))
  
  print("Generated password: ", final_pwd)


# Invoke your magic password generator
create_strong_password()
