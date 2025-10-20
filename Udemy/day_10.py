def math(a, b):
    return a + b

# print(math(1, 2))

def format_names(f_name, l_name):
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"

name_it = format_names("taeYEON", "kIM")
# print(name_it)

def greet(name):
    return f"Hello, {name}!"

# greet_this_user = greet("taeyeon")
# print(greet_this_user)

def square(a):
    return a ** 2

# print(square(5))

def check_number(a):
    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"

# print(check_number(4))
# print(check_number(5))

def convert_temp(a):
    c_temp = (a - 32) * 5/9
    return round(c_temp, 2)

to_celsius = convert_temp(100)
# print(to_celsius)

def convert_temp(a):
    return (a-32) * 5/9

celsius_result = convert_temp(100)
# print(f"{celsius_result:.2f}")

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
def count_vowels(word):
    num_vowels = 0
    for x in word:
        if x in vowels:
            num_vowels += 1
    return num_vowels

print(count_vowels("python"))
print(count_vowels("working until I retire"))