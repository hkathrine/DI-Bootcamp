#1
def get_input(parameter):
    while True:
        num = input(f"Please enter a {parameter}: ")
        try:
            val = int(num)
        except ValueError:
            print("The input is invalid")
            continue
        return val
    

number = get_input("number")
length = get_input("length")

num_list = [number * x for x in range(1,length + 1)]
print(num_list)

#2
str = input("please enter a string: ")

str_modified = []

current_letter = str[0]
str_modified.append(str[0])
for letter in str:
    if letter == current_letter:
        continue
    else:
        str_modified.append(letter)
        current_letter = letter

print("".join(str_modified))


