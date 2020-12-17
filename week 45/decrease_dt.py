# Problem E.4. Decrease the length of the time steps

import numpy as np
from math import cos
import matplotlib.pyplot as plt

class F:
    def __call__(self, x, t):
        return cos(6*t)/(1+t+x)

class ForwardEuler_v2:
    def __init__(self, f):
        self.f = f
    def set_initial_condition(self,U0):
        self.U0 = float(U0)
    def solve(self, time_points):
        """Compute solution for array of time points"""
        self.t = np.asarray(time_points)
        N = len(self.t)
        self.u = np.zeros(N)
        self.u[0] = self.U0
        # Time loop
        for n in range(N-1):
            self.n = n
            self.u[n+1] = self.advance()
        return self.u, self.t
    def advance(self):
        """Advance the solution one time step."""
        # Create local variables to get rid of "self." in # the numerical formula
        u, f, n, t = self.u, self.f, self.n, self.t
        #dt is not necessarily constant:
        dt = t[n+1]-t[n]
        unew = u[n] + dt*f(u[n], t[n])
        return unew

color = ["mistyrose", "plum", "lavenderblush", "lavender", "mediumpurple", "mediumslateblue", "slateblue", "indigo"]
c = 0

t_start = 0; t_end = 10
for n in [20,30,35,40,50,100,1000,10000]:
    time_points = np.linspace(t_start, t_end, n)

    f = F()
    solver = ForwardEuler_v2(f)
    solver.set_initial_condition(0)
    u,t = solver.solve(time_points)

    # print(f"Numerical Solution n={n}")
    # print("(u,    t)  ")
    # print("-----------")
    # results = list(zip(u,t))
    # print(*results, sep = "\n")
    # print()

    plt.plot(t, u, f"{color[c]}", label = f"n = {n}")
    plt.legend()
    plt.title("solutions for various n")
    plt.xlabel("time")
    c += 1
plt.show()

"""
(plot)
"""
