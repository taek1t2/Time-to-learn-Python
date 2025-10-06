import random
# from mimetypes import guess_type

word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)

placeholder = ""
num_of_word = len(chosen_word)
for character in range(num_of_word):
    placeholder += '_'
print(placeholder)

guess = input("Guess a letter: ").lower()


display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)
