import random
list_if_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728
count = 0
for i in range(20000):
    for j in range(20000 - i):
        if i != j and ((list_if_numbers[i] + list_if_numbers[i + j]) == target_number):
            count = count + 1
            print(f"{list_if_numbers[i]} and {list_if_numbers[j]} sums to the target number {target_number}")