# Problem E.5. Implement the explicit midpoint method

import numpy as np
from math import cos, sin, pi
import matplotlib.pyplot as plt

class ODESolver:
    def __init__(self, f):
        self.f = f
    def advance(self):
        """Advance solution one time step."""
        raise NotImplementedError # implement in subclass
    def set_initial_condition(self, U0):
        self.U0 = float(U0)
    def solve(self, time_points):
        self.t = np.asarray(time_points)
        N = len(self.t)
        self.u = np.zeros(N)
        # Assume that self.t[0] corresponds to self.U0
        self.u[0] = self.U0
        # Time loop
        for n in range(N-1):
            self.n = n
            self.u[n+1] = self.advance()
        return self.u, self.t

class ForwardEuler(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = t[n+1] - t[n]
        unew = u[n] + dt*f(u[n], t[n])
        return unew

class Midpoint(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = t[n+1] - t[n]
        k1 = f(u[n], t[n])
        k2 = f(u[n] + (dt*k1)/2, t[n] + dt/2)
        unew = u[n] + dt*k2
        return unew

f = lambda u, t: cos(t) - t*sin(t)
exact = lambda t: t*cos(t)
exact = np.vectorize(exact)

U0 = 0; N = 20; T = 4*pi
time_points = np.linspace(0,T,N)

# Forward Euler
fe = ForwardEuler(f)
fe.set_initial_condition(U0)
u1, t1 = fe.solve(time_points)
plt.plot(t1, u1, 'lavender', label = 'Forward Euler')

# Explicit midpoint method
m = Midpoint(f)
m.set_initial_condition(U0)
u2, t2 = m.solve(time_points)
plt.plot(t2, u2, 'purple', label = 'Explicit midpoint')


# Analytical solution
#plot the exact solution in the same plot
time_exact = np.linspace(0,T,301) #more points to improve the plot
plt.plot(time_exact, exact(time_exact), "red", label = "Exact solution")
plt.legend()
plt.title('Solution of the ODE u"=cos(t) - tsin(t), u(0)=0"')
plt.show()

"""
Drive code:

(A plot is made in this code (Solution of the ODE u"=cos(t) - tsin(t), u(0)=0").)
"""
