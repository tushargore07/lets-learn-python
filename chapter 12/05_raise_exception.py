#@ In order to prevent the basic mistakes we have to raise and error in our own codes. by using the(raise) option.

a= int(input("Enter the number:"))
b= int(input("Enter the number:"))

if(b==0):
    raise ZeroDivisionError("You have enterd a zero which will lead to not difined value ")

else :
   print(f"The division a/b is {a/b}")