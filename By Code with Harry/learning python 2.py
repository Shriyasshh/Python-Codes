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


#Readline()
'''
f=open('myfile.txt','r')
while True:
    line=f.readline()
    print(line)
    if not line:
        break
    print(line)
'''


'''
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
'''


#Writeline()

'''
f=open('myfile2.txt','w')
lines=['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()
'''
#seek(),tell()
'''
with open ('myfile.txt','r') as f:
        print(type(f))

        f.seek(5)
        print(f.tell())
        data=f.read(5)
        print(data)
'''


#truncate()

with open('myfile2.txt','w') as f:
    f.write("Hello World")
    f.truncate(8)

with open('myfile2.txt','r') as f:
        print(f.read())