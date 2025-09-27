from functools import reduce

# map example 
#@ it applies a func to all items in list 
#@ can use the lambda file 

l= [1,2,3,4,5]

square= lambda x:x*x
squarelist= map(square,l)
print(list(squarelist))

# filter example 
#@ kisi bhi list ko function ke according hum filter out kar sakte he 

def even(n):
    if (n%2==0):
        return True
    return False

onlyeven=filter(even,l)
print(list(onlyeven))

# reduce 
#@ it performs an activity function ko squentily pair of elements ke sath 

def add (a,b):
    sum= a+b
    return sum

def mul (a,b):
    out= a*b
    return out

a=reduce(mul,l)
s= reduce(add ,l)
print(s)
print(a)