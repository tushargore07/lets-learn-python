l=[1,2,3,4,5,55,50,15,35,23,56,7,8,45]

for itmes in l:

    def five(item):
        if item%5==0:
            return True
        return False

s= filter(five, l)
print(list(s))

