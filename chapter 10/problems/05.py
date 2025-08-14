from random import randint


class Train: 
     

     def __init__(self,trainno):
          self.trainno= trainno

     def book(self,fromm,to):
          print(f"Your ticket is booked in Train no {self.trainno} from {fromm} to {to}")
    
          
     def getstatus(self):
          print(f"Your Train no {self.trainno}is running on time")

     def fair (self,fromm,to):
          print(f"Your fair in train no {self.trainno} from {fromm}to {to} is {randint(299,1999)} ")


t= Train(1234)
t.book("nashik","pune")
t.fair("nashik","pune")
t.getstatus()
