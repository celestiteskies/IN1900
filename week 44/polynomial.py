# Problem 9.2. Implement Polynomials as a Class

#a)
class Quadratic():

    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def __call__(self, x):
        return self.a*x**2 + self.b*x + self.c
    def __str__(self):
        return f"{self.a}*x**2 + {self.b}*x + {self.c}"


#b)
class Cubic(Quadratic):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d

    def __call__(self, x):
        return super().__call__(x) + self.d*x**3

    def derivative(self):
        return f"{3*self.d}*x**2 + {2*self.a}*x + {self.b}"

    def __str__(self):
        return f"{3*self.d}*x**2 + {2*self.a}*x + {self.b} "

instance1 = Quadratic(1,3,2)
print(instance1)
print(f"x = 1: {instance1(1)} \nx = 2: {instance1(2)}")

print("\n")

instance2 = Cubic(1,3,2,4)
print(instance2)
print(f"x = 1: {instance2(1)} \nx = 2: {instance2(2)}")
print("Derivative:", instance2.derivative())


"""
Drive code:

1*x**2 + 3*x + 2
x = 1: 6
x = 2: 12


12*x**2 + 2*x + 3
x = 1: 10
x = 2: 44
Derivative: 12*x**2 + 2*x + 3
"""
