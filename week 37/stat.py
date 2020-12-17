# Problem 4.8. Simple Statistical Functions

import numpy as np
from math import sqrt

def mean(x_list):
    """function mean(x_list) that returns
    the mean value of a list of numbers
    """
    N = 0
    m = 0
    for i in range(1,len(x_list)+1):
        m = m + x_list[i - 1]
        N += 1
    return 1/N*m

def standard_deviation(x_list):
    """Standard deviation function: returns the standard deviation of a list of numbers"""
    s = 0
    x = 0
    for i in range(1,len(x_list)+1):
        x =(x_list[i - 1] - mean(x_list))**2
        s = s + x
    s_N = sqrt(1/len(x_list)*s)
    return s_N


#test functions:

def test_mean():
    """
    Verifies the mean function. Compares the returned value with the result from numpy.mean.
    """

    x_test_values = [0.699, 0.703, 0.698, 0.688, 0.701]
    x_list = x_test_values
    expected =np.mean(x_test_values)
    computed = mean(x_list)
    tol = 1E-14
    success = abs(expected - computed) < tol
#     print (success)
    msg = f"computed={computed}!={expected}(expected)"
#     print (msg)
    assert success, msg

def test_standard_deviation():
    """Tests the standard deviation function. Compares the returned value with the result from numpy.std."""

    x_test_values = [0.699, 0.703, 0.698, 0.688, 0.701]
    x_list = x_test_values
    expected =np.std(x_test_values)
    computed = standard_deviation(x_list)
    tol = 1E-14
    success = abs(expected - computed) < tol
    # print (success)
    msg = f"computed={computed}!={expected}(expected)"
#     print (msg)
    assert success, msg


if __name__ == "__main__":
    test_mean()

if __name__ == "__main__":
    test_standard_deviation()

"""pytest:
collected 2 items

stat.py ..                                                                 [100%]

============================== 2 passed in 0.13s ===============================
"""
