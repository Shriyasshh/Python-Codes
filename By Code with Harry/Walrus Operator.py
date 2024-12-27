'''
a=True
print(a:=False) #walrus operator ":="
'''

'''
no=[1,2,3,4,5]
while (n:=len(no))>0:
    print(no.pop())
'''


# foods=list()        #regular way
# while True:
#     food=input("Enter food name: ")
#     if food== "quit" :
#         break
#     foods.append(food)

foods=list()        #using walrus operator
while(food:=input("Enter food name: "))!="quit":
    foods.append(food)