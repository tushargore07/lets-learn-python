'''
stone= 1
paper=-1
scissors =0
'''
import random

computer=random.choice([1,-1,0])
yourstr= input("Enter your word: ")
you={"stone":1,"paper":-1,"scissors":0}
reversed= {1:"stone",-1:"paper",0:"scissors"}

source= you[yourstr]

print(f"You chose {reversed[source]}\ncomputer chose {reversed[computer]}")

if(computer==source):
    print("Its a draw")

else:
    if(computer==1 and source==-1):
        print("You win!")

    elif(computer==1 and source==0):
        print("You lose!")

    elif(computer==-1 and source==1):
        print("You lose!")

    elif(computer==-1 and  source==0):
        print("You win!")

    elif(computer==0 and source==1):
        print("You win!")

    elif(computer==0 and source==-1):
        print("You lose!")

    else:
        print("something went wronng ")

