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