# Problem E.7. Solve an ODE describing cooling of coffee

import numpy as np
import matplotlib.pyplot as plt
from ODESolver import ForwardEuler, RungeKutta4

#a)
class Cooling:
    def __init__(self, h, Ts):
        self.h = h
        self.Ts = Ts

    def __call__(self, T, t):
        dTdt = -self.h*(T - self.Ts)
        return dTdt

    def terminate(self, T, t, step_no):
        tol = 0.01*self.Ts # approach room temperature
        return abs(T[step_no]-self.Ts) < tol

def estimate_h(t1, Ts, T0, T1):
    pass
    h = (T1 - T0)/(t1*(Ts - T0))
    return h

#b)
if __name__ == "__main__":
    def test_Cooling():
        t1 = 15; Ts = 20; T0 = 95; T1 = 92
        h = estimate_h(t1, Ts, T0, T1)
        cool = Cooling(h, 20)
        dTdt = ForwardEuler(cool)

        t0 = (0, 15) #time points
        U0 = 95
        dTdt.set_initial_condition(U0)
        u, t = dTdt.solve(t0)
        tol = 1e-10
        expected = 92
        computed = u[1]
        assert np.abs(expected - computed) < tol

test_Cooling()

#c)
T0 = 95 #temperature when t=0 in C
t1 = 15; T1 = 92 #temperature after 15 seconds in C
U0 = T0

dt = t1; tstop = 3600
N = int (tstop/dt)
timepoints = np.linspace(0, tstop, N)

for color, Ts in zip([ "slateblue", "darkorange"], [20,25]):
    h = estimate_h(t1, Ts, T0, T1)
    cool = Cooling(h, Ts)
    dTdt = RungeKutta4(cool)
    dTdt.set_initial_condition(U0)
    u, t = dTdt.solve(timepoints, cool.terminate)
    print(f"Surrounding temperature: {Ts}. Coffee temperature when poured into the cup: {u[0]}◦C. After 15 sec: {u[1]}")
    plt.plot(t, u, f"{color}", label = f"Ts = {Ts}")


plt.legend()
plt.xlabel("time (seconds)")
plt.ylabel("Temperature (◦C)")
plt.title("Solutions-Newton’s law of cooling")
plt.show()


"""
(plot)
printed:

Surrounding temperature: 20. Coffee temperature when poured into the cup: 95.0◦C. After 15 sec: 92.04714889201496
Surrounding temperature: 25. Coffee temperature when poured into the cup: 95.0◦C. After 15 sec: 92.05135255632543
"""
