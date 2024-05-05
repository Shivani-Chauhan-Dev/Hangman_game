import random
import hangman_word

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
# word_list = ["mouse","banana","grapes","blue","cat","dog","sheep","girl"]
chosen_word = random.choice(hangman_word.word_list)
display = []
word_len = len(chosen_word)
for _ in range(word_len):
    display += "_"
print(display)
end_of_game = False
lives = 6
while not end_of_game:
    guess = input("guess a letter : ").lower()
    
    if guess in display :
        print(f"You have already guessed {guess}")


    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(stages[lives])


    if "_" not in display:
        end_of_game = True
        print("You win")
