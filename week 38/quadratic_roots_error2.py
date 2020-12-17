# Problem 5.4. Quadratic with raising Error

from math import sqrt

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
        print (f"The solution is x1 = {x1}")
    else:
        print (f"The solution is: {x1:5.4f}")
else:
    raise ValueError(f"The input values for a, b and c yield complex roots.")
    sys.exit(1)
#     if we want to compute the complex roots:
#     from cmath import sqrt
#     x1 = (-b + sqrt(b**2 -4*a*c))/2*a
#     x2 = (-b - sqrt(b**2 -4*a*c))/2*a
#     print (f"The solutions are complex numbers: {x1} and {x2}")


"""
for a = 1, b = 1, c = 1, prited on terminal:
ValueError: The input values for a, b and c yield complex roots.

for a = 1, b = 0, c = −1, printed on terminal:
The first solution is x1 = 1
The second solution is x2 = -1
"""
