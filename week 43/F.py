# Problem 8.3. Make a function class

import numpy as np
import matplotlib.pyplot as plt

class F:
    def __init__(self,m,n):
        self.m = m
        self.n = n

    def __call__(self, x):
        values = []
        for x in x:
            values.append(np.sin(self.n*x)*np.cos(self.m*x))
        return values

u = F(1,22)
v = F(13,50)
x = np.linspace(0, 2*np.pi, 51)

plt.plot(u(x), v(x))
plt.axis("equal")
plt.show()

"""
(plot)
"""
