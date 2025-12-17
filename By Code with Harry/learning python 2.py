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


# File IO

#Reading a file 
f=open('myfile.txt','r')
print(f.read())
f.close()

# writing a file

f=open('myfile.txt','w')
w=f.write("Hello World")
print(w)
f.close()


# Append a file

f=open('myfile.txt','a')
w=f.write(" Hello World")
f.close()



with open('myfile.txt','a') as f:
    f.write(" Hey I am inside with ")



#Readline()

f=open('myfile.txt','r')
while True:
    line=f.readline()
    print(line)
    if not line:
        break
    print(line)




i=0
while True: 
    i+=1
    line=f.readline()
    # print(line)
    if not line:
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])

    print(f"marks of student {i}in maths", m1*2)
    print(f"marks of student {i}in eng", m2*2)
    print(f"marks of student {i}in GK", m3*2)   



#Writeline()


f=open('myfile2.txt','w')
lines=['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()

#seek(),tell()

with open ('myfile.txt','r') as f:
        print(type(f))

        f.seek(5)
        print(f.tell())
        data=f.read(5)
        print(data)



#truncate()

with open('myfile2.txt','w') as f:
    f.write("Hello World")
    f.truncate(8)

with open('myfile2.txt','r') as f:
        print(f.read())



#Lambda Function

# def double(x):
#     return x*2

# print(double(5))

double=lambda x: x*2
print(double(5)) 

cube=lambda x: x**3
print(cube(5))


#Map filter reduce  

# always give soln of input

def cube(X):
    return X**3

l=[1,2,3,4,5,6,9]
cubes=list(map(cube,l))
print(cubes)

# map works as below
l=[1,2,3,4,5,6]
newl=[]
for i in l:
    newl.append(cube(i))

print(newl)

#Filter()
# gives output based on condition if true

def filter_function(a):
    return a>4
b=filter(filter_function,l)
print(b)
newnewl=list(filter(filter_function,l))
print(newnewl)



# Reduce()

from functools import reduce

no=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,no)
print(sum)


# is , ==   

a=4
b="4"
print(a is b ) #compares exact location of object in memory
print(a==b)     #compares value

c=[1,2,5]
d=[1,2,5]
print(c is d)
print(c==d)