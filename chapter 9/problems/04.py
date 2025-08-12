word= "donkey"

with open("04problem.txt") as f:
    content= f.read()

contentnew= content.replace(word,"####")

with open("04problem.txt","w")as f:
    f.write(contentnew)

