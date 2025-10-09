print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Selection Error: Please choose right input and try again.")

if pepperoni == "Y":
    if size == "small":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"You're final bill is {bill}")

# how to get the total? come back later

