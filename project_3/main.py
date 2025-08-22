import random 

n= random.randint(1,100)

Guesses=1 
a=-1
while(a!=n):
    a= int(input("Guess the number : "))
    
    if(a<n):
       print("Higher number please ")
       Guesses+=1 

    elif(a>n):
        print("Lower number please")
        Guesses=+1


print(f"Your have correct {n} number in {Guesses} guesses")