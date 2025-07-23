def func2(f):
    return 5*(f-32)/9

f=int(input("Enter the value: "))

c= func2(f)
print(f"{round(c,2)} °C")