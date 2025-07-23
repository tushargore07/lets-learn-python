'''
factorial(1)= 
factorial(2)=
factorial(3)=
factorial(4)=
factorial(5)=

'''

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n* factorial(n-1)

n= int(input("Enter number : "))
print(f"The factorial of this number is{factorial(n)}")
     

