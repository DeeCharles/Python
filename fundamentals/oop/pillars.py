class CoffeeM:
    def __init__(self,name):
        self.name = name
        self.water_temp = 200

    def brew_now(self,beans):
        print(f"Using {beans}!")
        print("Brew now brown cow!")

    def clean(self):
        print("Cleaning!")

#Abstraction
class Barista:
    def __init__(self,name):
        self.name = name
        self.cafe = CoffeeM("Cafe") 
        
    def make_coffee(self):
        self.cafe.brew_now()

my_barista=Barista("Dee")
print(f"My Baista name is {my_barista.name}")

# Inheritance and  Polymorphism
class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)

    def make_cappuccino(self,beans):
        super().brew_now(beans)
        print("Frothy!!!")

    def clean(self):
        print("Cleaning the froth")

my_choice=CoffeeM("Cappacuino")

my_choice.brew_now("Columbian")
my_choice.clean()

my_type=CappuccinoM(CoffeeM)
print(my_type)
my_type.make_cappuccino("Brazilian")
my_type.clean()