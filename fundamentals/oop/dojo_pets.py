# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method

from time import sleep


class Ninja:
    def __init__(self,first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        pet1.play()
        print("I want my",owner.pet_food+".")
        print(pet1.health)
        
        
    def feed(self):
        pet1.eat()
        print("Feeding", pet1.name, owner.pet_food)

    def bathe(self):
        pet1.noise()


# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound
class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 10
        self.energy = 5
        
    def sleep(self):
        self.energy+=25
        print(self.energy)

    def eat(self):
        self.energy +=5
        self.health +=10
        print(self.energy,self.health)
        

    def play(self):
        self.health += 5
        #print(self.health)

    def noise(self):
        print("roof roof")

pet1=Pet("Brownie","dog","stand on hind legs")
owner=Ninja("Bruce","Lee","ball","beef",pet1)

owner.walk()
owner.bathe()
owner.feed()
# pet1.eat()
# pet1.play
# pet1.noise()
print(owner.first_name, "is feeding" )



