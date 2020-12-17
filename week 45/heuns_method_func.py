# Problem E.6. Implement Heun’s method as a function

import numpy as np
from math import exp
import matplotlib.pyplot as plt

#a)
def heuns_method(f, U0, T, n):
    """Solve u'=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.zeros(n+1)
    u = np.zeros(n+1)  # u[k] is the solution at time t[k]
    u[0] = U0
    t[0] = 0
    dt = T/n

    for i in range(n):
        t[i+1] = t[i] + dt
        k1 = f(u[i], t[i])
        k2 = f(u[i] + dt * k1, t[i] + dt)
        u[i+1] = u[i] + dt*(k1*0.5 + k2*0.5)
    return u, t

#b)
def f(u,t):
    return 0.1*u

def exact(t):
    return U0*np.exp(0.1*t)

exact = np.vectorize(exact)


#u' = 0.1u
U0 = 0.1 #u(0) = 1
#solution: exp(t)
T = 1; N = 1

def test_heuns_against_hand_calculations():
    u,t = heuns_method(f, U0, T, N)
    hand = np.array([0.1, 0.1105])
    error = np.abs(hand - u).max()
    assert error < 1E-14, '|exact - u| = %g != 0' % error

test_heuns_against_hand_calculations()

#c)
T = 60; U0 = 0.1; N = 10
u,t = heuns_method(f,U0,T,N)
plt.plot(t, exact(t), label = "Analytical Solution")

color = ["mediumpurple", "mediumslateblue", "lavender"]
c = 0

for N in [10, 20, 100]:

    u,t = heuns_method(f,U0,T,N)

    plt.plot(t, u, f"{color[c]}", label = f"Numerical Solution, dt = {T/N}")

    plt.legend()
    plt.title("numerical and analytical solution")
    c+=1
plt.show()

"""
(plot)
"""
