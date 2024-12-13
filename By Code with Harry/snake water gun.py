x1=input("Enter your choice:")
x2= x1.lower()
# print(x2)
if x2=="snake":
    p=0
    
elif x2=="water":
    p=1
elif x2=="gun":
    p=2   
else:
    p=3

    
import random
com=[0,1,2]
no=random.choice(com)
name=["snake","water","gun"]
# print(name[no])

if p==3:
    print("Invalid input")
elif p==no:
    print(f"Since your input is {x2} and computer input is {name[no]}  their is Draw")
elif p==0 and no==1:
    print(f"Since your input is {x2} and computer input is {name[no]} you Win")
elif p==1 and no==2:
    print(f"Since your input is {x2} and computer input is {name[no]} you Win")
elif p==2 and no==0:
    print(f"Since your input is {x2} and computer input is {name[no]} you Win")

else:
    print(f"Since your input is {x2} and computer input is {name[no]} you Lose")