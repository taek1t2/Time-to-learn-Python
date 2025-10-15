import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# cards[0] = 1
random.shuffle(cards)

start_blackjack = input("Do you want to play a game of Blackjack? (y/n) \n").lower()
print("\n" * 25)

import blackjack_art
print(blackjack_art.logo)

player_hand = []
computer_hand = []

if start_blackjack == "y":
    first_draw = random.choice(cards)
    player_hand.append(first_draw)
    second_card = random.choice(cards)
    player_hand.append(second_card)
    current_score = sum(player_hand)
    print(f"Your cards: {player_hand}, current score: {current_score}")

    computer_first_card = random.choice(cards)
    computer_hand.append(computer_first_card)
    hidden_display = "_"
    another_card = random.choice(cards)
    computer_hand.append(another_card)
    puter_score = sum(computer_hand)
    print(f"Dealer's first card: {[computer_hand[0], hidden_display]}\n")

    hit_or_stand = input('Type "hit" to get another card OR type "stand" to pass: \n').lower()

    if hit_or_stand == "hit":
        draw_another_card = random.choice(cards)
        player_hand.append(draw_another_card)
        current_score = sum(player_hand)
        print(f"Your cards: {player_hand}, current score: {current_score}")
        print(f"Dealer's first card: {[computer_hand[0], hidden_display]}\n")

        if current_score == 21 and puter_score == 21:
            print("Blackjack!")
        elif current_score == 21 and puter_score > 21:
            print("Dealer busts - You win!")
        elif puter_score == 21 and current_score > 21:
            print("Players bust - You lose!")
        elif current_score <= 21 and puter_score <= 21 and current_score > puter_score:
            print("You win!")
        elif puter_score <= 21 and current_score <= 21 and current_score < puter_score:
            print("You lose!")

    elif hit_or_stand == "stand":
        draws_again = random.choice(cards)
        computer_hand.append(draws_again)
        puter_score = sum(computer_hand)
        print(f"Dealer's hand: {computer_hand}, Dealer's score: {puter_score}")

# game_continues = True
# while game_continues: