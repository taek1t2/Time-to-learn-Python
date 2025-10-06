# Step by Step with the instructor for coding this.
import random
from hangman_words import word_list
from hangman_art import logo, stages

lives = 6

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
num_of_word = len(chosen_word)
for character in range(num_of_word):
    placeholder += '_'

print("Word to guess: " + placeholder)

game_over = False
correct_characters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_characters:
        print(f"You've already guessed {guess}.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_characters.append(guess)
        elif letter in correct_characters:
            display += letter
        else:
            display += "_"

    print("word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lost a life.")
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}!YOU LOSE**********************")
    

    # my original thought process
    # guess_count = 0
    # game_art = stages
    # for life in range(lives):
    #     if guess != display:
    #         life -= 1
    #         guess_count = life
    #     print(f"You have {guess_count} guess(es) left. Think again!")
    #     print(game_art)
    # else:
    #     print("You ran out of guesses, you lose.")
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages)
