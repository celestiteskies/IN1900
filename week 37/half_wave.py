# Problem 4.5. Half-wave rectifier

from math import sin

def f(x):
    if x > 0:
        y = sin(x)
    else:
        y = 0
    return y

def test_fx():
    """
    Verify the function for two values of x (10 and -10), one that gives sinx < 0 and one where sinx > 0.
    """
    x = 10
    expected1 = -0.5440211108893699
    computed1 = f(10)
    # print(computed1)

    x = -10
    expected2 = 0
    computed2 = f(-10)
    # print(computed2)

    tol = 1E-14
    success = (abs(expected1 - computed1) < tol and abs(expected2 - computed2) < tol)
    msg = f"computed1={computed1}!={expected1}(expected1) and computed2={computed2}!={expected2}(expected2) "
    assert success, msg

if __name__ == "__main__":
    test_fx()


""" pytest in the terminal:
collected 1 item

half_wave.py .                                                           [100%]

============================== 1 passed in 0.01s ===============================
"""
