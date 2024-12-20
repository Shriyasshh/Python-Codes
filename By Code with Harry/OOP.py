'''
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
'''
#Constructors
'''
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
'''

#Decorators
'''
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
'''


# Getters & Setters
'''
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
'''

# Inheritance

'''
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
'''

# Access Modifiers
'''
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
'''

# Static method
'''
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
'''

#Instance & class vaiables
'''
class Employee:
    company_name="Apple"
    No_employees=0
    def __init__(self,name):
        self.name=name
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
'''


# Class Method
'''
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
'''

#Class methods as Alternative Constructor

'''
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
'''

# fun dir(),__dict__,help() methods
'''
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
'''

# Super Keyword
'''
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
'''


'''
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
'''
