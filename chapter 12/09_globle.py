#@ value of the variable outside the function is consider as globale value we can use that in both place out side as well as inside the func 

#@ with the help of globle func we can set a globle value particular variable which will be the full and finale value 


a= 90 

def fun(): 
    global a
    a=3
    print(a)

fun()
print(a)    