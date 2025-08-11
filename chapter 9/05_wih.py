f= open("file.txt")
print(f.read())

f.close()

#@ in order to not close the file 
#@ we use the with function 

with open ("file.txt") as f:
    print(f.read())

