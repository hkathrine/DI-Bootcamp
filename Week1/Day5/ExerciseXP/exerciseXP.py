
#1
print("ex 1 ---------------")

keys = ['Ten', 'Twenty', 'Thirty']

values = [10, 20, 30]

res = dict(zip(keys, values))

print(res)

print("--------------------")

#2
print("ex 2 ---------------")

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}

ticket_price_under_3 = 0
ticket_price_3_to_12 = 10
ticket_price_over_12 = 15

price = 0
total_cost = 0

for name, age in family.items():
    print(f"The price for {name} is", end=" ")
    if 3 <= age <= 12:
        price = ticket_price_3_to_12
    elif age < 3:
        price = ticket_price_under_3
    elif age > 12:
        price = ticket_price_over_12

    print(f"{price}")
    total_cost += price

print(f"Total is {total_cost}")

print("--------------------")

print("bonus---------------")

family_bonus = {}

while True:

    name = input("Please enter a name (for quiting print 'quit'): ")
    if name == "quit":
        break
    try:
        age = int(input("Please enter an age: "))
    except:
        print("Please enter a number")
        continue
    family_bonus[name] = age

price = 0
total_cost = 0

for name, age in family_bonus.items():
    print(f"The price for {name} is", end=" ")
    if 3 <= age <= 12:
        price = ticket_price_3_to_12
    elif age < 3:
        price = ticket_price_under_3
    elif age > 12:
        price = ticket_price_over_12

    print(f"{price}")
    total_cost += price

print(f"Total is {total_cost}")

print("--------------------")



#3
print("ex 3 ---------------")

brand = {"name": "Zara",
         "creation_date": 1975,
         "creator_name": "Amancio Ortega Gaona",
         "type_of_cothes": ["men", "women", "chilren", "home"],
         "international_competitors": ["Gap","H&M", "Benetton"],
         "number_stores": 7000,
         "major_color": {"France":"blue", "Spain":"red", "US":["pink", "green"]}}

brand["number_stores"] = 2

clients = ", ".join(brand["type_of_cothes"])
print(f"Zara's clients are looking for clothes for {clients}")

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

print(f"The last international competitor is {brand['international_competitors'][-1]}")

print(f"Major colors in the US: {brand['major_color']['US']}")

print(f"Number of keys: {len(brand)}")

print(f"All keys: {list(brand.keys())}")


print("--------------------")

#4
print("ex 4 ---------------")

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
indices = [0, 1, 2, 3, 4]

dict_1 = dict(zip(users, indices))
print(dict_1)

dict_2 = dict(zip(indices, users))
print(dict_2)

dict_3 = dict(zip(sorted(users), indices))
print(dict_3)

print("--------------------")