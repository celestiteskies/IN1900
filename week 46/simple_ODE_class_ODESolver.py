# Problem E.3. Solve a simple ODE with the ODEsolver hierarchy

import numpy as np
from math import exp
import matplotlib.pyplot as plt

#a)
print("""
Generic form: u' = f(u, t)

u -5u' = 0
u′ = u/5
f(u, t) = u/5

This equation has the general solution u = Ce^t for any constant C, so it has
an infinite number of solutions. Specifying the initial condition u(0) = 0.1 gives
C = 0.1, and we get the unique solution u = 0.1e^(t/5).
""")

#b)
def f(u, t):
    return u/5.0

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

#c)
class ForwardEuler(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = t[n+1] - t[n]
        unew = u[n] + dt*f(u[n], t[n])
        return unew


U0 = 0.1; T = 20; dt = 5
N = int(T/dt)

time_points = np.linspace(0,T,N)
fe = ForwardEuler(f)
fe.set_initial_condition(U0)
u, t = fe.solve(time_points)

# print(f"U0 = {U0}, T = {T}, dt = {dt}, N = {N}")
# print("Numerical Solution")
# print("(u,    t)  ")
# print("-----------")
# results = list(zip(u,t))
# print(*results, sep = "\n")

#d)
plt.plot(t, u, 'lavender', label = 'Numerical solution')
plt.title("Numerical vs Exact solution")

exact = lambda t:  U0*exp(0.2*t)
exact = np.vectorize(exact)

#plot the exact solution in the same plot
time_exact = np.linspace(0,T,301) #more points to improve the plot
plt.plot(time_exact, exact(time_exact), "red", label = "Exact solution")
plt.legend()
plt.show()


#e)
plt.plot(time_exact, exact(time_exact), "red", label = "Exact solution")

color = ["indigo", "slateblue", "mediumslateblue", "mediumpurple", "lavender"]
c = 0

for N in [4, 8, 20, 40, 1000]:
    time_points = np.linspace(0,T,N)
    fe = ForwardEuler(f)
    fe.set_initial_condition(U0)
    u, t = fe.solve(time_points)

    plt.plot(t, u, f"{color[c]}", label = f"dt = {T/N}")
    plt.legend()
    plt.title("Simulations for smaller ∆t")
    c += 1
plt.show()

"""
Drive code:
(2 plots are created.)

printed:

Generic form: u' = f(u, t)

u -5u' = 0
u′ = u/5
f(u, t) = u/5

This equation has the general solution u = Ce^t for any constant C, so it has
an infinite number of solutions. Specifying the initial condition u(0) = 0.1 gives
C = 0.1, and we get the unique solution u = 0.1e^(t/5).

"""
