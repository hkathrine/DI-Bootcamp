#ex 1

def display_massage():
    print("I am learsining about functions in Phyton")

display_massage()
#ex 2
def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Alice in Wonderland")

#ex 3

def describe_city(city = "Unknown", country = "Unknown"):
    print(f"{city} is in {country}")
describe_city()
print("\n")
describe_city("Haifa", "Israel")
describe_city("Israel")

#ex 4
import random
def compare_numbers(num):
    if (num > 100 or num < 1) :
        print("The number is out of range.")
    else:
        random_num = random.randint(1, 100)
        if num == random_num:
            print("Success!")
        else:
            print(f"Fail! Your number: {num}, Random number: {random_num}")    
    
compare_numbers(9)

compare_numbers(0)

compare_numbers(100)

#ex 5
def make_shirt(size = "large", text = "I love Python."):
    print(f"The size of the shirt is {size} and the text is {text}")
make_shirt()
make_shirt("medium")
make_shirt("medium", "none")

#ex 6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_names):
    for magician in magician_names:
        print(f"{magician}")

def make_great(magician_names):
    for i in range(len(magician_names)):
        magician_names[i] = magician_names[i] + " the Great"

make_great(magician_names)

show_magicians(magician_names)

#ex 7

def get_random_temp():
    return random.randint(-10, 40)

def main():
    random_temp = int(get_random_temp())
    print(f"The temperature right now now is {random_temp} degrees Celsius.")
    if random_temp < 0:
        print(f"Brr, that's freezing! Wear some extra layers today")
    elif random_temp <= 16:
        print(f"Quite chilly! Don't forget your coat.")
    elif random_temp <= 23:
        print(f"Nice weather.")
    elif random_temp <= 32:
        print(f"A bit warm, stay hydrated.")
    else:
        print(f"It's really hot! Stay cool.")

main()

def get_random_temp_bonus():
    return random.uniform(-10, 40)

def main_bonus():
    random_temp = float(get_random_temp_bonus())
    print(f"The temperature right now now is {random_temp} degrees Celsius.")
    if random_temp < 0:
        print(f"It is winter")
    elif random_temp <= 16:
        print(f"It's spring or fall")
    elif random_temp <= 32:
        print(f"It is summer")
    else:
        print(f"It's hell")

main_bonus()