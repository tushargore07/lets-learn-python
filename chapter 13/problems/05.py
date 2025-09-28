from functools import reduce

l=[1,2,3,4,5,55,50,15,35,23,56,7,8]

def greater(a,b):
    if(a>b):
        return a 
    return b 

print(reduce(greater,l))

