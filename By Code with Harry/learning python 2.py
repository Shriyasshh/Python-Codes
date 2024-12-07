#Global variable and local variable

x=7
print(x)

def hello():
    global x
    x=5
    y=1
    print(f"the local x is {x}")
    print("hello Bob")


print(f"the global x is {x}")
hello()
print(f"the global x is {x}")
# print(y)

