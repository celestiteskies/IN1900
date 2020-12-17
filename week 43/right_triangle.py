# Problem 8.2. Right triangle class

#a)
class RightTriangle:
    def __init__(self,a,b):
        from math import sqrt
        self.a  = a
        self.b = b
        c = sqrt(self.a**2 + self.b**2)
        self.c = c

    #if we want to print the information about the triangle sides
    def __str__(self):
        return f"The short triangle sides are: a = {self.a} and b = {self.b}. The hypotenuse is: c = {self.c}"

#b)
triangle1 = RightTriangle(1,1)
# print(triangle1)
print(triangle1.c)

triangle2 = RightTriangle(3,4)
# print(triangle2)
print(triangle2.c)


#c)
class RightTriangle:
    def __init__(self,a,b):
        from math import sqrt
        if a <=  0 or b <= 0:
            raise ValueError("The sides should not have negative or zero length.")
        else:
            self.a  = a
            self.b = b
            c = sqrt(self.a**2 + self.b**2)
            self.c = c

    def __str__(self):
        return f"The short triangle sides are: a = {self.a} and b = {self.b}. The hypotenuse is: c = {self.c}"

def test_RightTriangle():
    success = False
    try:
        triangle3 = RightTriangle(1,-1)
    except ValueError:
        success = True
    assert success

if __name__ == "__main__":
    test_RightTriangle()


#d)
class RightTriangle:
    def __init__(self,a,b):
        from math import sqrt
        if a <=  0 or b <= 0:
            raise ValueError("The sides should not have negative or zero length.")
        else:
            self.a  = a
            self.b = b
            c = sqrt(self.a**2 + self.b**2)
            self.c = c

    def __str__(self):
        return f"The short triangle sides are: a = {self.a} and b = {self.b}. The hypotenuse is: c = {self.c}"


    def plot_triangle(self):
        import matplotlib.pyplot as plt
        plt.plot([0,0,self.a,0], [0,self.b,0,0])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.axis('equal')
        return plt.show()

triangle2 = RightTriangle(3,4)
triangle2.plot_triangle()



"""
pytest in terminal:

collected 1 item

right_triangle.py .                                                                             [100%]

========================================== 1 passed in 0.01s ==========================================
"""



"""
printed:

(plot)

1.4142135623730951
5.0
"""
