# Problem 5.3. Quadratic with exceptions

import sys
from math import sqrt

try:
    a = sys.argv[1]
    a = float(a)
    while a == 0:
        a = input("Give a value different than zero:")
        a = float(a)
    b = sys.argv[2]
    b = float(b)
    c = sys.argv[3]
    c = float(c)
except IndexError: # if index error use input to ask the user for the missing input data.
    print ("No command line arguments for a b c values! Provide a b c:")
    try:
        #a shold not be zero
        a = input("Give value a:")
        a = float(a)
        while a == 0:
            a = input("Give a value different than zero:")
            a = float(a)
        b = input("Give value b:")
        c = input("Give value c:")
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        print(f"Something went wrong in reading input data! All three input values should be numbers. Try again!")
        exit()
    while a == 0:
        a = input("Give a value different than zero:")
        a = float(a)
    b = float(b)
    c = float(c)
except ValueError:
    print(f"Something went wrong in reading input data! All three input values should be numbers. Try again!")
    exit()

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
        x2= int(x2)
        print (f"The second solution is x2 = {x2}")
    else:
        print (f"The second solution is x2 = {x2:5.4f}")
#     print (f"The solutions are: {x1:5.4f} and {x2:5.4f}")
elif r == 0:
    x1 = -b/(2*a)
    if x1 ==int(x1):
        x1= int(x1)
        print (f"The solution is: x1 = {x1}")
    else:
        print (f"The solution is: {x1:5.4f}")
else:
    from cmath import sqrt
    x1 = (-b + sqrt(b**2 -4*a*c))/2*a
    x2 = (-b - sqrt(b**2 -4*a*c))/2*a
    print (f"The solutions are: {x1} and {x2}")
    

"""
for a = 3, b = -8, c = 1, it is printed on the terminal:
The first solution is x1 = 22.8167
The second solution is x2 = 1.1833

for a = 1, b = 1, c = 1, printed:
The solutions are: (-0.5+0.8660254037844386j) and (-0.5-0.8660254037844386j)

a = 1, b = 0, c = −1, printed:
The first solution is x1 = 1
The second solution is x2 = -1
"""
