# Problem 7.5. Interpret output from a program

import numpy as np
import matplotlib.pyplot as plt

def arrays(filename):
    with open(filename, "r") as file:
        delta_x = []
        abs_error = []
        n = []
        lines = file.readlines()
        for c in lines:
            split_lines = c.split(", ")
            delta_x.append(float(split_lines[0][9:]))
            abs_error.append(float(split_lines[3][11:]))
            n.append(int(split_lines[5][2:].strip()))
    delta_x = np.array(delta_x)
    abs_error = np.array(abs_error)
    n = np.array(n)
    return delta_x , abs_error, n

#call function-read file: approx.txt(output of: approx_derivative_sine.py)
delta_x, abs_error, n = arrays('approx.txt')

#Plot delta_x and abs_error versus n
plt.semilogy(n,abs_error)
plt.semilogy(n,delta_x)
plt.xlabel("n")
plt.legend(['abs_error', 'delta_x'])
plt.show()

print(
"""
As n increases, delta_x gets smaller and smaller(goes towards 0).
We observe that the approximation improves with decreasing delta_x until n = 8.
After that, the approximated values are greater than the exact value but really
close to it.

The abslolute error increases after n = 8 due to approximation errors.
The reason for the error increases at about delta_x = 10^−8 is that the total
error consists of contributions of both discretization and roundoff errors.

The discretization error decreases in an orderly fashion as delta_x decreases, and
it dominates the roundoff error when delta_x is relatively large.
But when delta_x gets below the approximate value 10^−8 the discretization error becomes
very small and roundoff error starts to dominate (i.e., it becomes larger in magnitude).
When n > 15, the approximated values are now set equal to zero and therefore,
the absolute error will equal the exact value,thus, remain constant for those n values.

""")

"""
printed:

As n increases, delta_x gets smaller and smaller(goes towards 0).
We observe that the approximation improves with decreasing delta_x until n = 8.
After that, the approximated values are greater than the exact value but really
close to it.

The abslolute error increases after n = 8 due to approximation errors.
The reason for the error increases at about delta_x = 10^−8 is that the total
error consists of contributions of both discretization and roundoff errors.

The discretization error decreases in an orderly fashion as delta_x decreases, and
it dominates the roundoff error when delta_x is relatively large.
But when delta_x gets below the approximate value 10^−8 the discretization error becomes
very small and roundoff error starts to dominate (i.e., it becomes larger in magnitude).
When n > 15, the approximated values are now set equal to zero and therefore,
the absolute error will equal the exact value,thus, remain constant for those n values.
"""
