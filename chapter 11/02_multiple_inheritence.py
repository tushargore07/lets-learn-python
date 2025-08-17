#@ here both the Employee and the codes are the parent/base of the class programmer 
#@ we also use the multiple class as a parent 
#@ all the content in the Employee and codes will work in the programmer 

class Employee:
    company= "ITC"
    def how(self):
        print(f"The name is {self.name} and the salary is {self.salary }")



class codes :
    language= "Python"
    print("Among all the laungage the python is the best ")



class programmer (Employee, codes):
    company= "TCS"
    def showlaunguage (self):
        print(f"The name is {self.name} and the salary is {self.salary }")


a= Employee()
b= programmer()


print(a.company, b.company)
