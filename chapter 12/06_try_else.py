#@ jab bhi try ke ander ki condition satisfy hogi to else ke ander ka code direct run hoga start ho jayega 
#@ lekin agar except run hota he to vo else ko run nahi karega 


try :
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))

except Exception as e :
    print(e)

else:
    print(f"The sum is {a+b}")


