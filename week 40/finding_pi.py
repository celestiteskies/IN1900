# Problem A.4. Finding π with Newton’s method

from math import sin, cos
import numpy as np

f = lambda x: np.sin(x)    #define the function to investigate
dfdx = lambda x: np.cos(x) #define its derivative
x0 = 3.14                  #set initial guess

def Newton(f, dfdx, x, tol, max_n):
    n=0 #initial number of iterations

    #print in a tidy way such that the values are easy to compare
    print(f"      χ                  Real π value          Difference(real-approximated π)")
    print(f"---------------------------------------------------------------------------")

    while abs(f(x)) > tol and n <= max_n:
        print(f"x{n}: {x:.13f} {np.pi:20.13f}  {np.abs(np.pi - x):20.13f}")
        x = x - f(x)/dfdx(x) #compute next x
        n += 1

    print(f"x{n}: {x:.13f} {np.pi:20.13f}  {np.abs(np.pi - x):20.13f}")

result = Newton(f, dfdx, x0, tol=1.0E-10, max_n=100)

"""
printed:

      χ                  Real π value          Difference(real-approximated π)
---------------------------------------------------------------------------
x0: 3.1400000000000      3.1415926535898       0.0015926535898
x1: 3.1415926549364      3.1415926535898       0.0000000013466
x2: 3.1415926535898      3.1415926535898       0.0000000000000
"""
