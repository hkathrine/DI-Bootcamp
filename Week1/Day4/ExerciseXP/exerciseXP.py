#1
print("1--------------------------------")

my_fav_numbers = {5, 25, 67, 99, 33}
print(my_fav_numbers)

my_fav_numbers.add(55)
my_fav_numbers.add(105)
print(my_fav_numbers)

my_fav_numbers.discard(105)
print(my_fav_numbers)

friend_fav_numbers = {1, 3, 2}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)


print(my_fav_numbers)
print(friend_fav_numbers)
print(our_fav_numbers)


#2
print("2--------------------------------")

tuple_1 = (1, 4)
print(tuple_1)

tuple_1 = tuple_1 + (5,)
print(tuple_1)

#3
print("3--------------------------------")

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
print("--------------------------------")


basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)

print("--------------------------------")

basket.append("Kiwi")
basket.append("Apples")
print(basket)

print("--------------------------------")

print(f"there are {basket.count("Apples")} Apples")

print("--------------------------------")

basket.clear()
print(basket)

#4
print("4--------------------------------")
numbers = [x / 2 for x in range(3,11)]
print(numbers)

final_numbers =[int(x) if x.is_integer() else x for x in numbers]
print(final_numbers)

#5
print("5--------------------------------")
for i in range(19):
    print(f"{i + 1}", end=" ")
print("---------")
for i in range(19):
    if i%2 == 0:
        print(f"{i + 1}", end=" ")
    
#6
print("6--------------------------------")
name = input("Please enter your name: ")
while True:
    if len(name) < 3:
        name = input("Give the corect name1: ")
    elif name.isdigit():
        name = input("Give the corect name2: ")
    else:
        print("thank you")
        break

#7
print("7--------------------------------")
input_fruits = input("Plaese enter your favorite fruits: ")
fruits_list = input_fruits.split()

fruit = input("Plaese enter a name of any fruit: ")

if fruit in fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

#8
print("8--------------------------------")
final_cost = 10
pizza_topping = []
toppings_cost = 2.5
while True:
    new_topping = input("Please enter a topping or type \'quit\' to quit: ")
    if new_topping == "quit":
        break
    else:
        print(f"Adding {new_topping} to your pizza")
        final_cost += toppings_cost
        pizza_topping.append(new_topping)
print(f"Toppings:", end=" ")
for i in range(len(pizza_topping)):
    print(f"{pizza_topping[i]}", end=" ")
print("\n")
print(f"Total cost is ${final_cost}")

#9
print("9--------------------------------")

price_under_3 = 0
price_3_to_12 = 10
price_over_12 = 15
total_cost_for_tickets = 0

while True:
    new_age = input("Please enter an age ofa person or type \'quit\' to quit: ")
    if new_age == "quit":
        break
    try:
        van = int(new_age)
    except ValueError:
        print("The input is invalid")
        continue
    if int(new_age) < 3:
        total_cost_for_tickets += price_under_3
    elif int(new_age) >= 3 and int(new_age) <= 12:
        total_cost_for_tickets += price_3_to_12
    else:
        total_cost_for_tickets += price_over_12

print(f"the total cost is ${total_cost_for_tickets}")
