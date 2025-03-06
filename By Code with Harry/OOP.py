
class Person:
    name="Bob"
    age=19
    occupation="Engineer"
    networth=100
    def info(self):
        print( f"{self.name} is a {self.occupation}")

a=Person()
a.name="John"
a.occupation="Doctor"
# print(a.name,a.occupation)
# print(a.networth)
a.info()

#Constructors

class Person:
    def __init__(self,n,o):
        print("hey i am a person")
        self.name=n
        self.occ=o

    def info(self):
        print( f"{self.name} is a {self.occ}")



a=Person("bob","engineer")
b=Person("john","doctor")
a.info()
b.info()


#Decorators

def greet(fun):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fun(*args,**kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello world")

@greet
def add(a,b):
    print(a+b)

greet(hello)()
# hello()
greet(add)(1,2)
# add(1,2)



# Getters & Setters

class Myclass:
    def __init__(self,value):
        self._value=value

    def show(self):
        print(f"Value is {self._value}")
    @property
    def ten_value(self):            #getter
        return 10*self._value
        
    
    @ten_value.setter               #setter
    def ten_value(self,new_value):
        self._value=new_value/10

obj=Myclass(10)
# print(obj.ten_value)
obj.ten_value=67
print(obj.ten_value)
obj.show()


# Inheritance


class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showDetails(self):
        print(f"The name of Employee : {self.id} is {self.name}")

class Programmer(Employee):     #Inheitance
    def showLanguage(self):
        print("Default language is Python")
        print(self.name)
e1=Employee("Bob",101)
e1.showDetails()

e2=Programmer("John mini",102)
e2.showLanguage()


# Access Modifiers

class Employee:
    def __init__(self):
        self.name="Bob"     #Public
        self._age=19        #Protected
        self.__salary=10000 #Private

a=Employee()
print(a.name)
print(a._age)
# print(a.__salary)         #Throws error
print(a._Employee__salary)    #For Accessing private variable


# Static method

class Math():
    def __init__(self,num):
        self.num=num

    def add2num(self,n):
        self.num=self.num+n

    @staticmethod
    def add(a,b):
        return a+b


result=Math.add(2,3)
print(result)
a=Math(5)
print(a.num)
a.add2num(10)
print(a.num)
print(a.add(2,3))   
#if static notused it show error of passing 3argument self,a,b


#Instance & class variables

class Employee:
    company_name="Apple"        #class variable
    No_employees=0
    def __init__(self,name):
        self.name=name          #instance variable
        self.raise_amount=1.04
        Employee.No_employees+=1
    def showDetails(self):
        print(f"The name of Employee is {self.name} and the raise amount in {self.No_employees} sized {self.company_name}  is {self.raise_amount}")

emp1=Employee("Bob")
emp1.raise_amount=2.05
emp1.company_name="apple india"
emp1.showDetails()
# Employee.showDetails(emp1)
e2=Employee("John")
e2.showDetails()
Employee.company_name="Microsoft"
print(Employee.company_name)



# Class Method

class Employee:
    company="Apple"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

    @classmethod
    def changecompany(cls,newcompany):
        cls.company=newcompany
    
e1=Employee()
e1.name="Bob"
e1.show()
e1.changecompany("Microsoft")
e1.show()
print(Employee.company)


#Class methods as Alternative Constructor


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
        
e1=Employee("Bob",10000)
print(e1.name)
print(e1.salary)


string="Bob-10000"
e2=Employee.fromstr(string)
# e2=Employee(string.split("-")[0],string.split("-")[1])
print(e2.name)
print(e2.salary)


# fun dir(),__dict__,help() methods

x=(1,2,3)
print(dir(x))
print(x.__add__)



class Person:
    def __init__(self,name,ages):
        self.name=name
        self.age=ages
        self.version=1
p=Person("Bob",20)
# print(p.__dict__)

print(help(Person))
print(help(str))


# Super Keyword

class Parentclass:
    def parent_method(self):
        print('This is a parent method')

class Childclass(Parentclass):
    def parent_method(self):
        print("Bob")
        super().parent_method()
    def child_method(self):
        print("This is a child method")
        super().parent_method()

child_obj=Childclass()
child_obj.child_method()
child_obj.parent_method()



class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang


R=Employee("Bob",101)
P=Programmer("Ram",574,"Python")

print(P.name)
print(P.id)
print(P.lang)



#Magic/Dunder methods


class Employee1:
    def __init__(self,name):
        self.name=name
    def __len__(self):
        i=0
        for c in self.name:
            i+=1
        return i

    def __str__(self):
        return (f"The name of Employee is {self.name}")
    
    def __repr__(self):
        return (f"The name of Employee is {self.name} repr ")

    def __call__(self):
        print("Hey I am good")


e=Employee1("Bob")
print(e.name)
print(len(e))
print(e)    #Make either __str__ or __repr__ as a comment 
            #to see the output 

# Method Overloading

class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
class circle(shape):
    def __init__(self,r,):
        self.r=r
        super().__init__(r,r)
        #super().method_name(arguments)

    def area(self):
        return 3.14*super().area()
        # return 3.14*self.r**2

    
sq=shape(2,2)
print(sq.area())
cir=circle(2)
print(cir.area())
#The super() function in Python is used to call methods 
# from a parent (or superclass) in a child(or subclass) class

# Operators Overloading

#allows you to define custom behavior for operators 
#(e.g., +, -, *, etc.) when used with objects of a user-defined class

class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,other):
        return vector(self.i+other.i,self.j+other.j,self.k+other.k)
v1=vector(1,2,3)
print(v1)

v2=vector(4,7,5)
print(v2)

print(v1+v2)
print(type(v1+v2))

# Single Inheritance

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


# Multiple Inheritance

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


# Hybrid inheritance

class Baseclass:
    pass
class Derived1(Baseclass):
    pass
class Derived2(Baseclass):
    pass
class Derived3(Derived1,Derived2):
    pass


# Hierarchical inheritance

class Baseclass:
    pass
class D1(Baseclass):
    pass
class D2(Baseclass):
    pass
class D3(D1):
    pass
class D4(D2):
    pass
