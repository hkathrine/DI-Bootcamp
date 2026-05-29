
import string
import random
import datetime
from faker import Faker

#ex 1
print("ex 1-----------")

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    def __str__(self):
        return f'{self.amount} {self.currency}s'
    def __repr__(self):
        return f'{self.amount} {self.currency}s'
    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                return self.amount + other.amount
            else:
                raise TypeError(f"Cannot add {self.currency} and {other.currency}")
        else:
            return self.amount + other
    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency == other.currency:
                self.amount += other.amount
                return self
            else:
                raise TypeError(f"Cannot add {self.currency} and {other.currency}")
        else:
            self.amount += other
            return self
    def __int__(self):
        return self.amount
        
        


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)

print(int(c1))

print(repr(c1))

print(c1 + 5)

print(c1 + c2)

print(c1)

c1 += 5

print(c1)

c1 += c2
print(c1)

#print(c1 + c3)

print("---------------")


#ex 3
print("ex 3-----------")

str_all_letters = string.ascii_letters
random_string = "" 

for i in range(5):
    random_char = random.choice(str_all_letters)
    random_string += random_char

print("The random string is:", random_string)

random_string_2 = "".join(random.choices(str_all_letters, k=5)) #another way

print("The random string (2nd way) is:", random_string_2)

print("---------------")

#ex 4
print("ex 4----------")

curr_date = datetime.datetime.now()
print("Current date is ", curr_date.strftime("%Y-%m-%d"))


print("---------------")


#ex 5
print("ex 5-----------")

curr_date_2 = datetime.datetime.now()
jan_1 = datetime.datetime(2027, 1, 1)

time_diff = jan_1 - curr_date_2

print(time_diff)

print("---------------")


#ex 6
print("ex 6-----------")

def minutes_count(birthday_str: str):
    birthday = datetime.datetime.strptime(birthday_str, "%d-%m-%Y")
    curr_date = datetime.datetime.now()
    time_diff = curr_date - birthday
    time_diff_in_minutes = time_diff.total_seconds() / 60
    print(time_diff_in_minutes)

minutes_count('1-1-2000')


print("---------------")

#ex 7
print("ex 7-----------")

users_list = []
fake = Faker()

def add_user(num_of_users):
    for i in range (num_of_users):
        user_dict = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users_list.append(user_dict)

add_user(5)
print("Users list:")
for user in users_list:
    print(user)
    print("--------")

print("---------------")