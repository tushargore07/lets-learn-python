#@ finally id function which will run by crossing all the boundries it run in try as well as in excpet.  
#@ in function we can see the real use case of finally 

#@ normal code me hum finally nahi lagayenge to chalega lekin function me agar hame code ko run karana he at any cost to hame finally usefull hoga 


try :
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))

except Exception as e :
    print(e)

else:
    print(f"The sum is {a+b}")

finally:
    print("Thank you")


def same():
    try :
        a=int(input("Enter a number: "))
        b=int(input("Enter a number: "))
        return

    except Exception as e :
        print(e)
        return
    
    
    finally:
     print("Thank you")
     return
    
same()