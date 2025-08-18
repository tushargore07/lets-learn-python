#@ here super func in def allow to call the init of parent class 


class Employee ():
    a= 1
    
    def __init__(self):
        print("Constructor employee")

class student(Employee):
    
    def __init__(self):
        
        print("Constructor student")

class parent(student):
    def __init__(self):
        super().__init__()
        print("Constructor parent")
        

a= parent()
