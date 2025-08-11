f= open("poem.txt")
content= f.read()

if ("twinkle"in content):
    print("The word twinkle is present")

else:
    print("The word twinkle is absent")

    
#print(content)