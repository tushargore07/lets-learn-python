#@ here with @classmethod either we apply the instance attribute 
#the value of classattibutes prints all time change the self to cls 

class Employee():
    a= 1

    @classmethod
    def show(cls):
        print(f"Class attribute is  {cls.a}")


e= Employee()
e.a=45

e.show()