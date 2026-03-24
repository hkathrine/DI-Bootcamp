
import random

from exerciseXP import Dog

print("ex 3-----------")
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    
    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        print(f"{self._name} plays with", end=" ")
        for name in args:
            if name == args[len(args) - 1]:
                print(f'{name}')
            else:
                print(f'{name}', end=", ")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f'{self._name} {random.choice(tricks)}')

#test 

my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()
print("---------------")