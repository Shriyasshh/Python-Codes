# Fibonacci Series
'''def fibonacci(n):
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

print(fib(8))'''


# Exception handling Ignore/skips Errors
'''a=(input("Enter a number:"))

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
    print("Index error")'''

# Finally Clause Gives output even if exception/error occurs
'''
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
'''

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