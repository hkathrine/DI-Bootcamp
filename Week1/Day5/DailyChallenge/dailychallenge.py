#1
print("ex 1 ---------------")

input_word = input("Please enter a word: ")

dict_word = {}

for i in range(len(input_word)):
    if input_word[i] in dict_word.keys():
        dict_word[input_word[i]].append(i)
    else:
        dict_word[input_word[i]] = [i]

print(dict_word)

print("--------------------")

#2
print("ex 2 ---------------")
def clean_data(param): #cleans data and returns the value
    string = list(param)
    num = ""
    for i in range(len(string)):
        if string[i] != '$' and string[i] != ',':
            num = num + string[i]

    try:
        val = int(num)
    except:
        return 0
    
    return val

def determine_affordable_items(items_purchase, wallet):
    basket = []
    for name, price in items_purchase.items():
        if price <= wallet:
            basket.append(name)
            wallet -= price
    if not basket:
        return 0
    else:
        return basket

def buy(items_purchase, wallet):
    wallet = clean_data(wallet)

    for item, price in items_purchase.items():#clean data for every value in the dictionary
        value = clean_data(price)
        if value != 0:
            items_purchase[item] = value
        else:
            print("Error")
            break

    basket = determine_affordable_items(items_purchase, wallet)
    if basket == 0:
        print("Nothing")
    else:
        sprint(sorted(basket))



print("1 case")
buy({"Water":"$1", "Bread":"$3", "TV":"$1,000", "Fertiliser":"$20"}, "$300")

print("2 case")
buy({"Apple":"$4", "Honey":"$3", "Fan":"$14", "Bananas":"$4", "Pan":"$100", "Spoon":"$2"}, "$100")

print("3 case")
buy({"Phone":"$999", "Speakers":"$300", "Laptop":"$5,000", "PC":"$1200"}, "$1")

print("--------------------")