# Problem E.2. Solve a simple ODE with class-based code

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
class F:
    def __call__(self, u, t):
        return u/5.0

#c)
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


U0 = 0.1; T = 20; dt = 5
N = int(T/dt)
time_points = np.linspace(0,T,dt)

f = F()
solver = ForwardEuler_v2(f)
solver.set_initial_condition(U0)
u,t = solver.solve(time_points)

print(f"U0 = {U0}, T = {T}, dt = {dt}, N = {N}")

print("Numerical Solution")
print("(u,    t)  ")
print("-----------")
results = list(zip(u,t))
print(*results, sep = "\n")

#d)
exact = lambda t:  U0*exp(0.2*t)
exact = np.vectorize(exact)

plt.plot(t, u, 'lavender', label = "Numerical solution")
plt.plot(t, exact(t), "red", label = "Exact solution" )
plt.title("Numerical vs Exact solution")
plt.legend()
plt.show()


#e)

plt.plot(t, exact(t), "red", label = "Exact solution" )

color = ["indigo", "slateblue", "mediumslateblue", "mediumpurple", "lavender"]
c = 0

for N in [4, 8, 20, 40, 100]:
    time_points = np.linspace(0,T,N)

    f = F()
    solver = ForwardEuler_v2(f)
    solver.set_initial_condition(U0)
    u,t = solver.solve(time_points)
    plt.plot(t, u, f"{color[c]}", label = f"dt = {T/N}")
    plt.legend()
    plt.title("Simulations for smaller ∆t")
    c += 1
plt.show()


"""
Drive Code:

Generic form: u' = f(u, t)

u -5u' = 0
u′ = u/5
f(u, t) = u/5

This equation has the general solution u = Ce^t for any constant C, so it has
an infinite number of solutions. Specifying the initial condition u(0) = 0.1 gives
C = 0.1, and we get the unique solution u = 0.1e^(t/5).

U0 = 0.1, T = 20, dt = 5, N = 4
Numerical Solution
(u,    t)
-----------
(0.1, 0.0)
(0.2, 5.0)
(0.4, 10.0)
(0.8, 15.0)
(1.6, 20.0)
"""
