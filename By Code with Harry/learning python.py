# Fibonacci Series

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

# Example usage
n = 10  # Change this value to generate more Fibonacci numbers
print(fibonacci(n))


def fib(n):
    if n==0 or n==1:
        return 1
    else:
        fi=[0,1]
        for i in range(2,n):
            fi.append(fi[i-1]+fi[i-2])
        return fi

print(fib(8))


# Exception handling Ignore/skips Errors

a=(input("Enter a number:"))

try:
    for i in range(1,11):
        print(f"int({a}) * {i} = {int(a)*i}")
except Exception as e:
    print(e)
print("End of program")

try:
    num=int(input("Enter any integer:"))
    b=[6,3]
    print(b[num])
except ValueError:
    print(" Number entered is not an integer.")
except IndexError:
    print("Index error")

# Finally Clause Gives output even if exception/error occurs

try:
    l=[1,5,7,9]
    i=int(input("Enter a index:"))
    print(l[i])
except IndexError:
    print("indexerror occured")
except:
    print("some error occured")
finally:                              #It is use full in function creation
    print("IAM ALWAYS EXECUTED")      # It is same as print("IAM ALWAYS EXECUTED") without function


def fun():
    try:
        l=[1,5,7,9]
        i=int(input("Enter a index:"))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:                              
        print("IAM ALWAYS EXECUTED")
    #print("IAM ALWAYS EXECUTED")


x=fun()
print(x)



#Custom Error Raising


a=int(input("Enter a number betwn 5 and 10:"))
if a<5 or a>9:
    raise ValueError("Number should be between 5 and 10")


# Short hand if else

a=350
b=3000
print("A") if a>b else print("=") if a==b else print("B")

print("9") if a>b else ""
print("10") if a<b else print("3")

c=7 if a>b else 5
print(c)



# Enumerate Function


marks=[2,5,7,9,10,5]

for i in marks:
    print(i)


for nos  in enumerate(marks,3):
    print(nos)


for index,mark  in enumerate(marks):
    print(index,mark)



# Importing in python

import math
result=math.sqrt(9)
print(result)

from math import sqrt,pi
from math import *

result=sqrt(9)*pi
print(result)

from math import pi, sqrt as sq
import math as m


print(dir(math))

from Bob import bob,Welcome
print(Welcome)
print(bob())


# if __name__ == "__main__"

import Bob
Bob.bob()
Bob.welcome()
