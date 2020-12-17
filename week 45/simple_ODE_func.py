# Problem E.1. Solve a simple ODE with function-based code

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

#c)
def ForwardEuler(f, U0, T, N):
    """Solve u’=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.zeros(N+1)
    u = np.zeros(N+1) # u[n] is the solution at time t[n]
    u[0] = U0
    t[0] = 0
    dt = T/N
    for n in range(N):
        t[n+1] = t[n] + dt
        u[n+1] = u[n] + dt*f(u[n], t[n])
    return u, t


U0 = 0.1; T = 20; dt = 5
N = int(T/dt)
print(f"U0 = {U0}, T = {T}, dt = {dt}, N = {N}")
u, t = ForwardEuler(f, U0, T, N)
print("Numerical Solution")
print("(u,    t)  ")
print("-----------")
results = list(zip(u,t))
print(*results, sep = "\n")

#d)
exact = lambda t:  U0*exp(0.2*t)
exact = np.vectorize(exact)
# print(exact(t), t)

plt.plot(t, u, 'lavender', label = "Numerical solution")
plt.plot(t, exact(t), "red", label = "Exact solution" )
plt.title("Numerical vs Exact solution")
plt.legend()
plt.show()


#e)
plt.plot(t, exact(t), "red", label = "Exact solution" )

color = ["indigo", "slateblue", "mediumslateblue", "mediumpurple", "lavender"]
c = 0

for dt in [5, 2.5, 1, 0.5, 0.01]:
    U0 = 0.1; T = 20
    N = int(T/dt)
    u,t = ForwardEuler(f, U0, T, N)
    plt.plot(t, u, f"{color[c]}", label = f"dt = {dt}")
    plt.legend()
    plt.title("Simulations for smaller ∆t")
    c += 1
plt.show()

"""
Drive code:

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
