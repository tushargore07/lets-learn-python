class Employee: 
    launguage="python"      
    salary= 120000


    def getinfo(self):
        print(f"The launguage is {self.launguage} and the salary is {self.salary}")

    
#@ here this func does not need to be called 
    def __init__(self,name,launguage,salary):
        print("hello")
        self.name= name
        self.launguage= launguage
        self.salary= salary

#@ we have to put thing here as per the not init func 
tushar= Employee("tushar","java",130000)
    

print(tushar.name ,tushar.launguage, tushar.salary)
