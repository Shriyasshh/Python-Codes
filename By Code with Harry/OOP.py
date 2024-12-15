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