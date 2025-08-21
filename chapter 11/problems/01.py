class TwoDVectore:
    def __init__(self,i,j):
        self.i= i
        self.j= j

    def show(self):
        print(f"The TwoDVecote is {self.i}i+{self.j}j")


class ThreeDVectore(TwoDVectore):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k= k

    def show(self):
        print(f"The ThreeDVecote is {self.i}i+{self.j}j+{self.k}")

a=TwoDVectore(1,2)
a.show()
b= ThreeDVectore(1,2,3)
b.show()