class Employee: 
    launguage="py" # this is a class attribute
    salary = 1200000

tushar= Employee()
tushar.name= "Tushar" # This is an instance attribute 
print(tushar.name, tushar.launguage, tushar.salary)

harry=Employee()
harry.name="Harry"
print(harry.name, harry.launguage, harry.salary)

# here name is instance attribute and salary and launguage 
# class attribute as they directly belong to the class