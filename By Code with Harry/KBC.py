'''Create a program capable of displaying questions to the user like a KBC.
Use list data type to store the questions and their answers 
Display the final amount the person is taking home after playing the game.
'''

ques=["What is the full form of CPU?","What is the full form of GPU?","What is the full form of RAM?","What is the full form of ROM?"]
ans= ["Central processing unit,graphics processing unit, random access memory, read only memory"]
i=0
for i in range(len(ques)):
    print(ques[i])
    a=input("Give your answer.")
    if i==0:
        print("Your answer is correct:",a,"You have won ",10**i )
    else:
        sum=0
        j=0
        while j<=i:
            sum =sum + 10**j
        print("your answer is Wrong :",a, "Correct Answer is ",ans[i],"You Lost /n Total won:",sum) 
    i+=1

    




'''
    if ans[i]==a:
        print("Your answer is correct:",ans[i],"You have won ",10**i )
    else:
        sum=0
        j=0
        while j<=i:
            sum =sum + 10**j
        print("your answer is Wrong :",a, "Correct Answer is ",ans[i],"You Lost /n Total won:",sum)
    i+=1
print("Thank you for playing")'''