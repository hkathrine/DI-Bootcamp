import random


list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728
count = 0

seen_numbers = {}

for num in list_of_numbers:
    complement = target_number - num
    
    if complement in seen_numbers:
        count += seen_numbers[complement]
    
    # Запоминаем текущее число
    seen_numbers[num] = seen_numbers.get(num, 0) + 1

print(f"Total pairs found: {count}")