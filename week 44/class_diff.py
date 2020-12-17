# Problem 8.7. Numerical approximations of the derivative

import numpy as np
from math import sin, cos, pi
import matplotlib.pyplot as plt

#a)
class Diff:
    def __init__(self, f):
        self.f = f

    def diff1(self, x ,h):
        return (f(x+h) - f(x))/h

    def diff2(self,x, h):
        return (f(x+h) - f(x-h))/(2*h)

    def diff3(self,x , h):
        return (-f(x+2*h) + 8*f(x+h) - 8*f(x-h) + f(x-2*h))/(12*h)

#b)
h = [ 0.9, 0.6, 0.3, 0.1]
x = np.linspace(-1,1,1000) #x ∈ [−1,1]

f1 = lambda x: sin(2*pi*x) #function to differentiate
f = np.vectorize(f1)

inst = Diff(f) #create instance

#exact
f_diff = lambda x : 2*pi*cos(2*pi*x) #exact derivarive of function f
exact = np.vectorize(f_diff)
exact_values = exact(x)

for i in range(len(h)):
    d1 = ((inst.diff1(x, h[i])))
    d2 = ((inst.diff2(x, h[i])))
    d3 = ((inst.diff3(x, h[i])))

    #exact derivative plot
    plt.plot(x, exact_values,'r',label='True Value')
    plt.legend()

    #approximated plots
    plt.title(f'Accuracy, h = {h[i]}')
    plt.plot(x, d1, 'b', label= 'diff1')
    plt.plot(x, d2, 'purple', label= 'diff2')
    plt.plot(x, d3, 'c', label= 'diff3')
    plt.legend()
    plt.show()

    """

    printed:

    (4 plots)
    """
