#@ creating a new class from parent/Base class
#@ created new class also called child class


class Employee:
    company= "ITC"
    def how(self):
        print(f"The name is {self.name} and the salary is {self.salary }")


# class programmer(Employee) :
#     company= "Wipro"
#     def show (self):
#         print(f"The name is {self.name} and the salary is {self.salary }")


#     def showlaunguage (self):
#         print(f"The name is {self.name} and the salary is {self.salary }")



#@ Here Employee is parent class and programmer is child 
#@ all things of Employee will be in the programmer and also addditional of programmer will continue 


class programmer (Employee):
    company= "TCS"
    def showlaunguage (self):
        print(f"The name is {self.name} and the salary is {self.salary }")


a= Employee()
b= programmer()


print(a.company, b.company)
