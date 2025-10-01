rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_with_hands = [rock, paper, scissors]
player1 = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. ")
import random

choose_number = [rock, paper, scissors]

if player1 == "0":
    print(choose_number[0])
    print(random.choice(list_with_hands))
elif player1 == "1":
    print(choose_number[1])
    print(random.choice(list_with_hands))
elif player1 == "2":
    print(choose_number[2])
    print(random.choice(list_with_hands))
else:
    print("Number error. Choose only 0, 1, 2")

