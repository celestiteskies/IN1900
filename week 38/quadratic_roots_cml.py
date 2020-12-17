# Problem 5.2. Quadratic with command line

import sys
from math import sqrt

a = sys.argv[1]
a = float(a)
b = sys.argv[2]
b = float(b)
c = sys.argv[3]
c = float(c)

if a == 0:
    raise ValueError(f"The formula is not valid for a=0. Try another number.")
    sys.exit(1)

r = b**2 - 4*a*c

if r > 0:
    x1 = (-b + sqrt(b**2 -4*a*c))/2*a
    x2 = (-b - sqrt(b**2 -4*a*c))/2*a
    if x1 ==int(x1): #check if solution is a whole number
        x1= int(x1)
        print (f"The first solution is x1 = {x1}")
    else:
        print (f"The first solution is x1 = {x1:5.4f}")
    if x2 ==int(x2):
        x2 = int(x2)
        print (f"The second solution is x2 = {x2}")
    else:
        print (f"The second solution is x2 = {x2:5.4f}")
#     print (f"The solutions are: {x1:5.4f} and {x2:5.4f}")
elif r == 0:
    x1 = -b/(2*a)
    if x1 == int(x1):
        x1 = int(x1)
        print (f"The solution is x1 = {x1}")
    else:
        print (f"The solution is: {x1:5.4f}")
else:
    from cmath import sqrt
    x1 = (-b + sqrt(b**2 -4*a*c))/2*a
    x2 = (-b - sqrt(b**2 -4*a*c))/2*a
    print (f"The solutions are complex numbers: x1 = {x1} and x2 = {x2}")



""" for a = 1, b = -5, c =1, it is printed on the terminal:

The first solution is x1 = 4.7913
The second solution is x2 = 0.2087

for a = 1, b = 1, c = 1, printed:
The solutions are complex numbers: x1 = (-0.5+0.8660254037844386j) and x2 = (-0.5-0.8660254037844386j)

for a = 1, b = 0, c = -1, printed:
The first solution is x1 = 1
The second solution is x2 = -1
"""
