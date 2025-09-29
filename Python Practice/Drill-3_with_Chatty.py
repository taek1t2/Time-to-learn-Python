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
# scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "Diana": 60}

# for key, value in scores.items():
#     if value > 80:
#         print(key)
        
# scores["Eve"] = 95
# print(scores)


#Classes and objects
# class Car:
#     def __init__(self, make, model, year):
#         self.make = "Toyota"
#         self.model= "Camry"
#         self.year= 2008
    
#     print(f"{self.make} {self.model} {self.year}")

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model= model
#         self.year= year
    
#     def infoDisplay(self):
#         print(f"{self.make} {self.model} {self.year}")

# car1 = Car("Toyota", "4runner", 2017)
# car2 = Car("Hyundai", "Elantra", 2008)

# car1.infoDisplay()
# car2.infoDisplay()

#String manipulation

# def message(Python):
#     print(Python.upper())

#     print(Python[::-1])

#     sentence = Python.split()
#     print(len(sentence))


# message("Python is fun")

# def message(sentence):
#     print(sentence.upper())
#     print(sentence[::-1])
#     print(len(sentence.split()))

# message("Coding is challenging but fun at the same time.")

# numbers = [4, 9, 16, 25, 36, 49, 64]

# greater_than_20 = [num for num in numbers if num > 20]
# print(greater_than_20)

# odd_numbers = [num for num in numbers if num % 2 != 0]
# print(odd_numbers)

# numbers = [9, 4, 16, 25, 36, 49, 64]

# greaterThan20 = [num for num in numbers if num > 20]
# print(greaterThan20)

# odd_numbers = [num for num in numbers if num % 2 != 0]
# print(odd_numbers)


#len method with the input method
# question = input("What's your name?")
# print(len(question))

# print(input("How old are you?"))

print("Welcome to the Band Name Generator.")
location_question = input("Where did you grow up?\n")
pet_name = input("What's your cat's name?\n")

print("Your band name could be: " + location_question + " " + pet_name + "!")





