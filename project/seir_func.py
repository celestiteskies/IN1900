# Modeling Covid19 scenarios in Norway
# Final project IN1900, fall 2020
#(python3)

# Problem 1.1. The SEIR model as a function
import numpy as np
import matplotlib.pyplot as plt
from ODESolver import *

#a)
def SEIR(u,t):
    beta = 0.5; r_ia = 0.1; r_e2=1.25;
    lmbda_1=0.33; lmbda_2=0.5; p_a=0.4; mu=0.2;

    S, E1, E2, I, Ia, R = u
    N = sum(u)
    dS  = -beta*S*I/N - r_ia*beta*S*Ia/N - r_e2*beta*S*E2/N
    dE1 = beta*S*I/N + r_ia*beta*S*Ia/N + r_e2*beta*S*E2/N - lmbda_1*E1
    dE2 = lmbda_1*(1-p_a)*E1 - lmbda_2*E2
    dI  = lmbda_2*E2 - mu*I
    dIa = lmbda_1*p_a*E1 - mu*Ia
    dR  = mu*(I + Ia)
    return [dS, dE1, dE2, dI, dIa, dR]

def test_SEIR():
    tol = 1e-10
    u = [1, 1, 1, 1, 1, 1]
    t = 0

    computed = SEIR(u,t)
    computed = np.array(computed)
    expected = np.array([-0.19583333333333333, -0.13416666666666668, -0.302, 0.3, -0.068, 0.4])
    success = abs((expected - computed) < tol).all()
    msg = f"computed={computed}!={expected}(expected)"
    assert success, msg

if __name__ == "__main__":
    test_SEIR()

#b)
def solve_SEIR(T,dt,S_0,E2_0):
    N = int(round(T/float(dt)))
    time_points = np.linspace(0, T, N+1)

    E1_0 = 0; I_0 = 0; Ia_0 = 0; R_0 = 0

    U0 = [S_0, E1_0, E2_0, I_0, Ia_0, R_0]

    solver = RungeKutta4(SEIR)
    solver.set_initial_condition(U0)
    solution = solver.solve(time_points)
    u = solution[0]; t = solution[1]

    return u, t

#c)
def plot_SEIR(u,t):

    S = np.array(u)[:,0]; E1 = np.array(u)[:,1]; E2 = np.array(u)[:,2];
    I = np.array(u)[:,3]; Ia = np.array(u)[:,4]; R = np.array(u)[:,5]

    #The plot shows the dynamics of the categories S, I, Ia, and R.
    plt.plot(t,S,label='S')
    # plt.plot(t,E1,label='E1')
    # plt.plot(t,E2,label='E2')
    plt.plot(t,I,label='I')
    plt.plot(t,Ia,label='Ia')
    plt.plot(t,R,label='R')
    plt.legend()
    plt.title('SEIR model')
    plt.xlabel('time (days)')
    plt.ylabel('population')
    return plt.show()

#d)
#Solution of the SEIR model.
u, t = solve_SEIR(100, 1, 5e6, 100)
# print("The solution of the SEIR model is:")
# print(f"u: {u}")
# print(f"t: {t}")

plot = plot_SEIR(u, t)


"""
Drive code:
python3 seir_func.py

(plot)
"""
