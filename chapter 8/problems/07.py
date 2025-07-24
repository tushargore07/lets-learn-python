
def rem(l,word):
    n=[]
    for item in l:
        if not(item== word):
            n.append(item.strip(word))
    return n 

l= ["Tushar","Soham","Rohan","an"]

print(rem(l,"an"))