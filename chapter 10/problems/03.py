class Demo ():
    a= 4

o = Demo() # Here we prints the class atrribute no instance value is set 
              
print(o.a) 

o.a=0       # Here we set the instance value 
print(o.a)  # No original class value changed 