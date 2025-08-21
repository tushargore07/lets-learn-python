class Vectore :
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self,other):
        Result=Vectore (self.x+other.x,self.y+other.y,self.z+other.z)
        return Result
    
    def __mul__(self, other):   # Dot Product
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

V1= Vectore(1,2,3)
V2= Vectore(4,5,6)
V3= Vectore(7,8,9)

print("Addition:", V1 + V2)
print("Dot Product:", V1 * V2)