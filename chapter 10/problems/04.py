class calculater:
    def __init__(self,n):
        self.n=n 

    @staticmethod
    def greet():
        print("hello to everyone")


    def square (self):
        print(f"The square is {self.n*self.n}")

    def cube (self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot (self):
        print(f"The squarerooot is {self.n**1/2}")



a= calculater(4)
a.greet()
a.square()
a.cube()
a.squareroot()
