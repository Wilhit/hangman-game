#Hangman
import os
import random
import hangman_words
import hangman_art

lives = 6

display = []
stages = hangman_art.stages
word_list = hangman_words.word_list

logo = hangman_art.logo

print(logo)

chosen_word = random.choice(word_list)

word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system('cls')

    if guess in display:
        print(f"You've already guessed: {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
##        print(f"Current Position: {position} \nCurrent letter: {letter}\nGuessed letter: {guess}")
        if letter == guess:
            print(f"You guessed: {guess}")
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print()
        print(f"Your guessed {guess}, that's not in the word. You lose a life.")
        print()
        if lives == 0:
            end_of_game = True
            print("You lose")
            print()
            input("Press enter to exit")

            
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")
        print()
        input("Press enter to exit")

    print(stages[lives])
