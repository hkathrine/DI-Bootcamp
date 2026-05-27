


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




#ex 2
print("ex 2-----------")

print("---------------")


#ex 3
print("ex 3-----------")

print("---------------")

#ex 4
print("ex 4----------")

print("---------------")


#ex 5
print("ex 5-----------")

print("---------------")


#ex 6
print("ex 6-----------")

print("---------------")

#ex 7
print("ex 7-----------")

print("---------------")