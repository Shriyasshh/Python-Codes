import random

target=random.randint(1,100)
56

while True:
    userNO=input("Guess  the number: or Quit(Q):")
    if userNO=="Q" :

        break

    userNO=int(userNO)
    if( userNO== target):
        print("Your guess is Correct")
        break
    elif(userNO<target):
        print("Your guess is too low")
    elif(userNO>target):
        print("Your guess is too high")
    else:
        print("Wrong input")

print("Game Over")