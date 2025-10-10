# my version


from calculator_logo import logo
print(logo)
welcome = input("Hi! I'm a basic calculator. Click 'Enter' to continue")
print(welcome)

user_choose = input("Please select an operation: '+', '-', '*', '/'\n")

n1 = int(input("Input the first number: "))
n2 = int(input("Input the second number: "))

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

if user_choose in operations:
    chosen_function = operations[user_choose]
    answer = chosen_function(n1, n2)
    print(answer)

to_continue_more = True
while to_continue_more:
    continue_calculating = input("Do you want to perform another calculation? ('y'/'n') \n").lower()
    if continue_calculating == "y":
        n1 = answer
        user_choose = input("Please select an operation: '+', '-', '*', '/'\n")
        n2 = int(input("Input the second number: \n"))
        if user_choose in operations:
            chosen_function = operations[user_choose]
            answer = chosen_function(n1, n2)
            print(answer)
    else:
        to_continue_more = False
        print(f"This is your final answer: {answer}")


# The instructor version
import calculator_logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](4, 8))


def calculator():
    print(calculator_logo.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()