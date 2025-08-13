# The instance attribute has the preference over class attribute

class Employee: 
    launguage="python"      # this is a class attribute
    salary = 1200000

tushar= Employee()
tushar.launguage= "Java"    # This is an instance attribute
tushar.name= "Tushar" 

print(tushar.name, tushar.launguage, tushar.salary)
