class programmer:
    company="Microsoft"

    def __init__(self,name,salary,pincode):
        self.name= name
        self.salary= salary
        self.pincode= pincode


p= programmer("tushar",12000000,422004)
print(p.name,p.company,p.salary,p.pincode)

r= programmer("Rohan",100000,422004)
print(r.name,r.company,r.salary,r.pincode)
    
