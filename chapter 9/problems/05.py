words= ["donkey","bad","bura","ghatiya"]

with open("05problem.txt") as f:
    content= f.read()


for word in words:
    content= content.replace(word,"#"*len(word))

with open("05problem.txt","w")as f:
    f.write(content)
