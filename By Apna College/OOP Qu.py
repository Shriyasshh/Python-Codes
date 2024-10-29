#Define a Circle class to create a cirlce with radius r using the construcrtor.
#Define an area() method of the class which calculates the area of the circle.
# define a perimeter() method of the class which allows you to calculate the perimeter of the circle.  

'''class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def Area(self):
        area=Circle.pi*self.radius*self.radius
        print(area)
    def Perimeter(self):
        peri=2*Circle.pi*self.radius
        print(peri)


c1=Circle(15)
c1.Area()
c1.Perimeter()'''



# Define a Employee class with attributes role, department & salary. This class also has showDetails() method.
#  Create an Engineer class that inherits properties from Employee & attributes: name & age.
'''class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def Showdetail(self):
        print("Role=",self.role)
        print("Department=",self.dept)
        print("Salary=",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer", "IT", "75000")
e1=Engineer("Bob",32)
e1.Showdetail()'''


#Create a class called Order which storesvitems and its price.
#use Dunder function __gt__() to convey that:
#order1>order2 if price of order1>price of order2

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,o2):
        return self.price>o2.price 

o1=Order("chips",20)
o2=Order("cola",10)
print(o1>o2)