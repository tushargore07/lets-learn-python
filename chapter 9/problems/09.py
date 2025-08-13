with open ("this.txt") as f:
    content= f.read()

with open ("thiscopy.txt") as f :
    content1= f.read()


if (content == content1):
    print("They are identical ")

else:
    print("They are not identical ")

    