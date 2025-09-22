#@ when we took an particular input from the user and the user enters the wrong detais whole code is going to crash becuase of that. So here top prevent this we use the try and exception concept.And we can also show type of error to use.


try:
    a= int(input("Enter the number:"))
    print(a)

except ValueError as f:
    print(f)
except Exception as e:
    print(e)

print("Thank you ")