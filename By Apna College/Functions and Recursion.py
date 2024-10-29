'''a=5
b=10                  #values cant be changed.
sum=a+b 
print(sum)'''

'''def cal_sum(a,b):#a,b are parameters
    sum=a+b 
    print(sum)
    
    
cal_sum(2,4) #2,4 =arguments
cal_sum(4,8)'''


'''def cal_sum(a,b):
    return a+b 

sum =cal_sum(122,254)
print(sum)'''


'''def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()'''

#average of 3 nos
'''def cal_avg(a,b,c):
    sum =a+b+c 
    avg=sum/3
    print(avg)
    return avg

cal_avg(2,4,8)

average=cal_avg(3,6,9)
print(average)'''


'''print("shriyash")
print("dharkar")'''


'''print("shriyash",end =" ") #sep=" "  #makes 2 lines into one
print("dharkar")  #end="/n"'''



'''def cal_prod(a=1,b=1): #(a,b=2) only possible
    print(a*b)
    return a*b

cal_prod()'''



'''def cal_length(a):
    b=len(a)
    print(b)
    
cal_length("cutout")'''

#WAF to print the length of a list.(list is the parameter)
cities =["mumbai"," delhi" ,"pune" ,"nagpur", "wardha"]
hero =["thor","ironman" ,"spiderman"]

'''def print_len(list):
    print(len(list))
    
print_len(cities)

print_len(hero)'''


#WAF to print the elements of a list in a single line
'''def print_name(list):
    for val in list:
        print(val,end=" ")


print_name(hero)'''



#WAF to find the factorial of n.(n is parameter)

'''def cal_fact(a):
    x=1
    for val in range(1,a+1):
        x*=val 
    print(x)
    
cal_fact(6)'''

#WAF to convert USD to INR

'''def cal_curr(USD):
    INR= USD*83
    print(USD,"USD =",INR,"INR")
    
cal_curr(2)'''




'''def cal_no(a):
    if (a%2==0):
        print("no is Even")
    else:
        print("no is Odd")

cal_no(2)'''



                    #Recursion

#print n to 1.
'''def show(n):
    if (n==0):
        return 
    print(n)
    show(n-1)

show(5)'''

#print n!
'''def fact(n):
    if (n==1 or n==0):
        return 1 
    return fact(n-1)*n

print(fact(3))'''



#Write a recursive function to calculate the sum of first n natural numbers.


'''def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1) +n
    
sum =cal_sum(3)
print(sum)'''



#Write a recursive function to print all elements in a list. Hint: use list & index as parameters

'''def print_list(list,idx=0):
    if(idx ==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

cities =["mumbai","delhi" ,"pune" ,"nagpur", "wardha"]
print_list(cities,)'''


















