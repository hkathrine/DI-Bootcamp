#ex1
print("Hello world/nHello world/nHello world/nHello world/n")
#ex2
res = 99*99*99*8
#ex3

if 5<3: #false
    print("true")
else: 
    print("false")

if 3==3: #true
    print("true")
else: 
    print("false")

#if 3=="3": #
#    print("true")
#else: 
#    print("false")

#if 3<"3": #false
#    print("true")
#else: 
#    print("false")

if "Hello"=="hello": #false
    print("true")
else: 
    print("false")


#ex4
computer_brand = "Acer"

print(f"I have {computer_brand} computer.")

#ex5

name = "Kathrine"
age = 23
shoe_size = 37
info = f"My name is {name}. I'm {age} years old. My shoe size is {shoe_size}."
print(info)

#ex6

a = 7
b = 0

if a>b:
    print("Hello World")

#ex7
num = int(input("Please enter a number: "))
if (num % 2) == 0:
    print(f"The number {num} is even")
else:
    print(f"The number {num} is odd")


#ex8

my_name = "Kathrine"
your_name = input("Please enter your name: ")
if my_name == your_name:
    print("You are an egg")
else:
    print("You are a tomato")

#ex9

height = input("Please enter your heght in centimeters")

if int(height) > 145 :
    print("You are tall enough to ride")
else:
    print("You are not tall enough to ride")