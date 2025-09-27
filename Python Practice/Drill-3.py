# Practice writing code
# Task: Write a program that prints the numbers from 1 to 50.

# If the number is divisible by 3, print "Fizz".

# If divisible by 5, print "Buzz".

# If divisible by both, print "FizzBuzz".

# for x in range(1, 50):
#     if x % 3 == 0 and x % 5 == 0:
#         print("FizzBuzz")
#     elif x % 3 == 0:
#         print("Fizz")
#     elif x % 5 == 0:
#         print("Buzz")
#     else:
#         print(x)

# Given numbers that are even and create a new list of squares in numbers

# numbers = [3, 7, 12, 18, 25, 30]
# squares = []

# for i in numbers:
#     if i % 2 == 0:
#         print(i)

# for i in numbers:
#     squares.append(i ** 2)

# print(squares)


# Write a function that takes a person's name as input and prints: "Hello, <name>! Welcome to Python practice."

# def greet(name):
#     print(f"Hello, {name}! Welcome to Python practice!")

# name = ["Tae", "Dan", "Ann", "Diana"]

# for n in name:
#     greet(n)

# # OR

# def greet(name):
#     print(f"Hello, {name}! Welcome to Python practice!")

# greet("Jacquelyn")
# greet("Kristyn")


# Dictionary
scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "Diana": 60}

for key, value in scores.items():
    if value > 80:
        print(key)
        
scores["Eve"] = 95
print(scores)




