with open ("old.txt") as f:
    content= f.read()

with open ("renamed_by _python.txt","w"):
    f.write(content)