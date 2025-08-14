class Employee: 
    launguage="python"      
    salary= 120000
#in order to put the func we have use the self in func.

    def getinfo(self):
        print(f"The launguage is {self.launguage} and the salary is {self.salary}")


#@static function is used as a decorative 
    @staticmethod  # it alows us to not give the object to func
    def info():
        print("Good Morning")
    

tushar= Employee()
tushar.launguage= "Java"    
tushar.getinfo() # this can also be written as follow
Employee.getinfo(tushar)


print( tushar.launguage, tushar.salary)