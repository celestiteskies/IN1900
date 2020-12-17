#Problem 2.4 (find_roots.py, side 4) fra oppgaveheftet

import cmath           #import complex math module

a = 6
b = -5
c = 1

d = (b**2) - (4*a*c)  # calculate the discriminant

x1 = (-b-cmath.sqrt(d))/(2*a)
x2 = (-b+cmath.sqrt(d))/(2*a)

print (f"The solutions are {x1.real:.2f}, {x2.real:.2f}.")

"""
printed:
The solutions are 0.33, 0.50.
"""
