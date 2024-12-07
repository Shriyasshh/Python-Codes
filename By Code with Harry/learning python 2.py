#Global variable and local variable
'''
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
'''

# File IO

#Reading a file 
'''f=open('myfile.txt','r')
print(f.read())
f.close()
'''
# writing a file
'''
f=open('myfile.txt','w')
w=f.write("Hello World")
print(w)
f.close()
'''

# Append a file
'''
f=open('myfile.txt','a')
w=f.write(" Hello World")
f.close()
'''

'''
with open('myfile.txt','a') as f:
    f.write(" Hey I am inside with ")
    '''