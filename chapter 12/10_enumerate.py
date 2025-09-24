l = [1,23,45,67,234,345]


# items= 1
# for item in l :
#     print(f"The item number at index {items} is {item}")
#     items +=1

#@ to avoid this kind of code we use the enumerate method 


for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")