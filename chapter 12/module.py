def myFunc():
    print("Hello World!!")

#@__name__ is type  jis file me code likha he ussi se run karenge to main ayega ya ya kisi aur file me import karke run karenge to parent(jisme code likha ho ) file ka naam ayega 

if __name__ == "__main__":
    print("we are directly runnig from parent file ")
    #@ IT MEANS THAT CODE IS DIRECTLY EXECUTED BY THE FILE IT PRESENT IN 
myFunc()
print(__name__)

