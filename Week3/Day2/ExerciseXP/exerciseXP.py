
#1
print("ex 1-----------")
class Pets():
    def __init__(self, animals):
        self.animals = animals
    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def walk(self):
        return f'{self._name} is just walking around'

class Siamese(Cat):
    pass

class Bengal(Cat):
    pass

class Chartreux(Cat):
    pass



all_cats = [Bengal("Dori", 1), Chartreux("Pie", 5), Siamese("Sonya", 10)]

#let's pint each cat's name and age
for cat in all_cats:
    print(cat.get_name(), end=" ")
    print(cat.get_age())

sara_pets = Pets(all_cats)

sara_pets.walk()

print("---------------")

#2
print("ex 2-----------")

class Dog():
    def __init__(self, name, age, weight):
        self._name = name
        self._age = age
        self._weight = weight
    def bark(self):
        return f'{self._name} is barking'
    def run_speed(self):
        return self._weight / self._age * 10
    def fight(self, other_dog):
        if (self.run_speed() > other_dog.run_speed()):
            return f'{self._name} won the fight'
        else:
            return f'{other_dog._name} won the fight'

dog_1 = Dog("Rex", 2, 10)

dog_2 = Dog("Pixie", 5, 5)

dog_3 = Dog("Baron", 3, 150)

print(dog_1.bark())
print(dog_2.run_speed())
print(dog_1.fight(dog_2))

print("---------------")

#4
print("ex 4-----------")

class Person():
    def __init__(self, first_name, age, last_name = ""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False
        
class Family():
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age, self.last_name)
        self.members.append(new_person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"You are over 18, your parents Jane and John accept that you will go out with your friends.")
                    return
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                    return
        print(f"There is no {first_name} in this family")

    def family_presentation(self):
        print(f"The family's last name is {self.last_name}")
        for member in self.members:
            print(f"{member.first_name} is {member.age}")

family_Smith = Family("Smith")

family_Smith.born("Fred", 18)
family_Smith.born("Lexi", 0)     
family_Smith.born("Rex", 17)     
family_Smith.born("Lucy", 25)      

family_Smith.check_majority("Fred")
family_Smith.check_majority("Lexi")
family_Smith.check_majority("Ron")

family_Smith.family_presentation()
print("---------------")