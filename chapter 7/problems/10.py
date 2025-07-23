

'''
***
* *
*** 

'''



n= int(input("Enter the number:"))

for i in range(1,n+1):
    if(i==1 or i==n):             #for first and last line
        print("*"*n,end="")

    else:
        print("*",end="")         # for the center line 
        print(" "*(n-2),end="") 
        print("*",end="")
    print("")

    
