# Class
'''class Student:
    name ="Karan"
s0=Student()
print 
s1 = Student()
print(s1.name)
s2= Student()
print(s2.name)'''


'''class Cars:
    color="blue"
    brand="mercedes"

car1=Cars()
print(car1.color)
print(car1.brand)'''



# Constructor(init)

#Default Constructor
'''class Student:
    def __init__(self):
        pass
    
    
    #parameterized constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("adding new student in database")
    
s1 = Student("karan",89)
print(s1.name,s1.marks)

s2 =Student("arjun",98)
print(s2.name ,s2.marks)'''

#       Attributes
'''class Student:
    college_name="ABC College"  # if same value in all data
    name="anonymous"            # class attribute
    def __init__(self,name,marks):
        self.name=name               #different values in all data
        self.marks=marks             #object attribute
        print("adding new student in database")


s1 = Student("karan","87")
print(s1.name)

s2 = Student("karan",89)
print(s2.name,s2.marks)
print(Student.college_name)'''

#           Method
'''class Students:
    college_name="ABC College"  

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def Welcome(self):
        print("welcome student" ,self.name )
    def get_marks(self):
        print("your marks",self.marks)


s1=Students("karan",89)
s1.Welcome()
s1.get_marks()'''

#Create student class that takes name & marks of 3 subjects as arguments in constructor.
#then create a method to print the average.
'''class Student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    
    def average(self):
        print((self.mark1+self.mark2+self.mark3)/3)

s1=Student("ram",3,3,3)
s1.average()'''

#Or

'''class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for i in self.marks:
            sum += i
        print("hi",self.name,"your avg score :",sum/3)

s1=Student("ram",[89,97,68])
s1.get_avg()'''

#Static Methods
'''class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def hello():
        print("hello")
    def get_avg(self):
        sum=0
        for i in self.marks:
            sum += i
        print("hi",self.name,"your avg score :",sum/3)

s1=Student("ram",[89,97,68])
s1.get_avg()
s1.hello()'''

#Abstraction
'''class Car:
    def __init__(self):
        self.acc= False
        self.brk=False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.acc=True
        print("car started")

car1=Car()
car1.start()'''

#Create Account class with 2 attributes - balance and account no
#Create methods for debit ,credit &printing the balance 

'''class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.accno=acc
    #debit
    def debit(self,amount):
        self.balance-=amount
        print("Rs",amount,"was debited")
        print("total balance", self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"was credited")
        print("total balance", self.get_balance())


    def get_balance(self):
        return self.balance
    
acc1=Account(10000,12345)
acc1.debit(2000)
acc1.credit(5000)'''


# delete  data in object
'''class Student:
    def __init__(self,name):
        self.name=name

s1=Student("Arpit")
print(s1.name)
del s1.name
print(s1.name)'''

#Private attributes and methods
'''class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass    #__ is used to make data private

    def reset_pass(self):
        print(self.__acc_pass)


acc1=Account("12345","abcde")

print(acc1.acc_no)
print(acc1.reset_pass())'''


'''class Person:
    __name="annonymous"

    def  __hello(self):
        print("hello person")
    
    def welcome(self):
        self.__hello()



p1=Person()
print(p1.welcome())'''


# Inheritance
#Single Inheritance
'''class Car:
    color="black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")


class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("fortuner")
car2=ToyotaCar("prius")
print(car1.color)'''

#Multilevel Inheritance
'''class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")


class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type=type


car1=Fortuner("diesel")
car1.start()'''

#Multiple Inheritance
'''class A :
    varA="welcome to class A"
class B:
    varB="welcome to class B"
class C(A,B):
    varC="welcome to class C"

c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)'''

#Super Method
class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")


class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().start()

car1=ToyotaCar("prius","electric")
print(car1.type)


#Class Method
'''class person:
    name="anonymous"

    def changename(self,name):
        #person.name=name
        #self.__class__.name=name #(is used to give output same from data inside and outside of the object)
        self.name=name  #not possible unless @classmethod is used 

    #@classmethod
    def changename2(cls,name):
        cls.name=name
p1=person()
p1.changename("karan")
print(p1.name)
#print(person.name)

p2=person()
p2.changename2("shivam")
print(p2.name)
print(person.name)'''


#Property
'''class Student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths

    #def calculatepercentage(self):
    #    self.percentage=str((self.phy+self.chem+self.maths)/3) +"%"

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.maths)/3) +"%"
    
stu1=Student(70,80,90)
print(stu1.percentage)

stu1.phy=79
print(stu1.percentage)'''

#Polymorphism
'''class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def shownumber(self):
        print(self.real,"i",self.img,"j")

    def __add__(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return Complex(newreal,newimg)
    
    def __sub__(self,num2):
        newreal=self.real-num2.real
        newimg=self.img-num2.img
        return Complex(newreal,newimg)


num1=Complex(3,4)
num1.shownumber()

num2=Complex(7,5)
num2.shownumber()
#num3=num1.add(num2)
#num3.shownumber()

num3=num1+num2
num3.shownumber()

num4=num1-num2
num4.shownumber()'''