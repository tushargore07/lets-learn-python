#@ IT is just an basic example multilevel 


class Employee ():
    a= 1

class student(Employee):
    b= 2

class parent(student):
    c= 3

o= student()
print(o.a)