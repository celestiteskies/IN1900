# Problem E.8. Compare numerical methods for solving ODEs

from math import sin, cos, pi
import numpy as np
import matplotlib.pyplot as plt
from ODESolver import*

#a)
class Midpoint(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        k1 = f(u[k], t[k])
        k2 = f(u[k] + (dt*k1)/2, t[k] + dt/2)
        unew = u[k] + dt*k2
        return unew

class Heun(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        k1 = f(u[k], t[k])
        k2 = f(u[k] + dt * k1, t[k] + dt)
        unew = u[k] + dt*(k1*0.5 + k2*0.5)
        return unew

#b)
f = lambda u, t: t*cos(t) - sin(t)
exact = lambda t: t*sin(t) + 2*cos(t)
exact = np.vectorize(exact)


U0 = 2
T = 8*pi
n = [20, 25, 50, 150]

time_exact = np.linspace(0,T,301) #more points to improve the exact plot
color = ["lavender", "olive", "mediumslateblue", "b--"]




#            Heun method, Analytical for various n
c = 0
#analytical solution
plt.plot(time_exact, exact(time_exact), "red", label = "Exact solution")
for n in [20, 25, 50, 150]:
    time_points = np.linspace(0,T,n)

    #numerical solution
    h = Heun(f)
    h.set_initial_condition(U0)
    u1, t1 = h.solve(time_points)

    plt.title("Heun")
    plt.plot(t1, u1, f'{color[c]}', label = f'N = {n}')
    plt.legend()
    c+= 1

plt.show()




#            Explicit midpoint method, Analytical for various n
c = 0
#analytical solution
plt.plot(time_exact, exact(time_exact), "red", label = "Exact solution")
for n in [20, 25, 50, 150]:
    time_points = np.linspace(0,T,n)

    #numerical solution
    m = Midpoint(f)
    m.set_initial_condition(U0)
    u2, t2 = m.solve(time_points)

    plt.title("Explicit midpoint method")
    plt.plot(t2, u2, f'{color[c]}', label = f'N = {n}')
    plt.legend()
    c+= 1

plt.show()




#           4th order Runge-Kutta method, Analytical for various n
c = 0
#analytical solution
plt.plot(time_exact, exact(time_exact), "red", label = "Exact solution") # Analytical solution
for n in [20, 25, 50, 150]:
    time_points = np.linspace(0,T,n)

    #numerical solution
    rk = RungeKutta4(f)
    rk.set_initial_condition(U0)
    u3, t3 = rk.solve(time_points)

    plt.title("4th order Runge-Kutta")
    plt.plot(t3, u3, f'{color[c]}', label = f'N = {n}')
    plt.legend()
    c+= 1

plt.show()

"""
Drive code:
(3 plots)
(We notice that the Explicit midpoint method seems to provide the best results overall.)
"""
