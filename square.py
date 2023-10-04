import math

class square():
    def __init__(self,area):
        self.a = area

    def area(self):
        return (self.a * self.a)

    def perimeter(self):
        return(self.a*4)

if __name__=='__main__':
    s = square(5)
    print("The side of the square is 5")
    print("The area of Square is ", + s.area())
    print("The perimeter of Square is ", + s.perimeter())
    
