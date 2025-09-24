a= int(input("Enter the number: "))

list=[1,2,3,4,5,6,7,8,9,10]

table=[i*a for i in range(1,11)]

# c=open("filemm.text","w")
# c.write(str(table))

with open ("filemmm.txt" ,"w") as f:
    f.write(str(table))



print(table)