# Problem 5.1. Quadratic with user input

from math import sqrt

while True:
    try:
        #a shold not be zero
        a = input("Give value a:")
        a = float(a)
        while a == 0:
            a = input("Give a value different than zero:")
            a = float(a)
        b = input("Give value b:")
        c = input("Give value c:")
        b = float(b)
        c = float(c)
        break
    except ValueError:
        print("No valid value! Each value input should be a number. Please try again ...")

r = b**2 - 4*a*c    #discriminant

if r > 0:
    x1 = (-b + sqrt(b**2 -4*a*c))/2*a
    x2 = (-b - sqrt(b**2 -4*a*c))/2*a
    print (f"The solutions are: {x1} and {x2}")
elif r == 0:
    x1 = -b/(2*a)
    print (f"The solution is: {x1}")
else:
    from cmath import sqrt
    x1 = (-b + sqrt(b**2 -4*a*c))/2*a
    x2 = (-b - sqrt(b**2 -4*a*c))/2*a
    print (f"The solutions are complex numbers: {x1} and {x2}")


""" for a = 4, b = -8, c = 1 , it is printed on the terminal:
The solutions are: 29.856406460551018 and 2.1435935394489825

for a = 1, b = 1, c = 1, printed:
The solutions are complex numbers: (-0.5+0.8660254037844386j) and (-0.5-0.8660254037844386j)

a = 1, b = 0, c = −1, printed:
The solutions are: 1.0 and -1.0
"""
