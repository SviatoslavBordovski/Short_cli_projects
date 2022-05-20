import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

#Create underscore blanks
display = []
for _ in range(word_length):
    display += "_"

while "_" in display:
  guess = input("Guess a letter: ").lower()
  
  #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
      print("Guessed, continue...")
  if guess not in chosen_word:
    lives -= 1
    print(stages[lives])
  if lives == 0:
    print("You lose.")
  elif word_length == len(display) and "_" not in display:
    word = f"{''.join(display)}"
    print("Wohooo! Guessed word => ", word)
