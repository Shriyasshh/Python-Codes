# Single Inheritance
'''
class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def make_sound(self):
        print(f"Sound made by the animal.")


class dog(animal):      # Inheriting the animal class
    def __init__(self,name,breed):
        animal.__init__(self,name,species="Dogs")
        self.breed=breed

    def make_sound(self):
        print("Barks!")

d=dog("tommy","deshi")
d.make_sound()

a=animal("tommy","deshi")
a.make_sound()
'''

# Multiple Inheritance
'''
class Employee:
    def __init__(self,name):
        self.name=name
    
    def show(self):
        print(f"Name: {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"Dance: {self.dance}")

class Dancer_Employee(Dancer,Employee):
    def __init__(self,name,dance):
        self.name=name
        self.dance=dance


i=Dancer_Employee("Tommy","Hip-Hop")
print(i.name,i.dance)
print(i.show())
print(Dancer_Employee.mro())
'''

# Multilevel Inheritance

class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def show(self):
        print(f"name:{self.name}")
        print(f"species:{self.species}")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed

    def show(self):
        Animal.show(self)
        print(f"Breed:{self.breed}")

class GoldenRetriever(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,breed="Golden Retriever")
        self.color=color

    def show(self):
        Dog.show(self)
        print(f"Color:{self.color}")

g=GoldenRetriever("Tommy","Golden")
g.show()
print(GoldenRetriever.mro())