# Problem 1.3. The SEIR model across regions

import numpy as np
import matplotlib.pyplot as plt
from ODESolver import *
from SEIR import *

#a)
class RegionInteraction(Region):
    def __init__(self, name, S_0, E2_0, lat, long):

        super().__init__(name, S_0, E2_0)

        # convert from degrees  to radians
        self.lat = lat * np.pi / 180
        self.long = long * np.pi / 180

    def distance(self, other): #calculates the distance between the self region (i) and another region (j)
        R_Earth = 6.4    #in units of 10^6 m

        long_i = self.long              # φi
        long_j = other.long             # φj other longitude

        lat_i = self.lat               # λi
        lat_j = other.lat              # λj other latitude
        Δσ = np.arccos(np.sin(lat_i) * np.sin(lat_j) + np.cos(lat_i) * np.cos(lat_j) * np.cos(np.abs(long_i - long_j)))

        if self == other:
            return 0
        else:
            return R_Earth * Δσ


#b)
class ProblemInteraction(ProblemSEIR):

    def __init__(self, region, area_name, beta, r_ia = 0.1, r_e2=1.25, lmbda_1=0.33,
                 lmbda_2=0.5, p_a=0.4, mu=0.2):

        #region: list of regions
        #area_name: text string with name of total region

        self.area_name = area_name
        super().__init__(region, beta, r_ia, r_e2, lmbda_1, lmbda_2, p_a, mu)

    def get_population(self):
        N = [region.population for region in self.region]
        N = np.sum(N)
        return N


    def set_initial_condition(self):
        self.initial_condition = []
        for r in self.region:
            self.initial_condition += [r.S_0, r.E1_0, r.E2_0, r.I_0, r.Ia_0, r.R_0]
        return self.initial_condition

    def __call__(self, u, t):
        n = len(self.region)

        # create a nested list:
        # SEIR_list[i] = [S_i, E1_i, E2_i, I_i, Ia_i, R_i]:
        SEIR_list = [u[i:i+6] for i in range(0, len(u), 6)]

        # Create separate lists containing E2 and Ia values:
        E2_list = [u[i] for i in range(2, len(u), 6)]
        Ia_list = [u[i] for i in range(4, len(u), 6)]

        derivative = []
        for i in range(n):
            S, E1, E2, I, Ia, R = SEIR_list[i]

            dS = 0
            for j in range(n):
                E2_other = E2_list[j]
                Ia_other = Ia_list[j]
                N_j = sum(SEIR_list[j])
                dS += -self.r_ia * self.beta(t) * S * Ia_other / N_j * np.exp(-self.region[i].distance(self.region[j]))
                dS += -self.r_e2 * self.beta(t) * S * E2_other / N_j * np.exp(-self.region[i].distance(self.region[j]))

            # calculate dE1, dE2, dI, dIa, dR
            dE1 = -dS - self.lmbda_1 * E1
            dE2 = self.lmbda_1 * (1 - self.p_a) * E1 - self.lmbda_2 * E2
            dI = self.lmbda_2 * E2 - self.mu * I
            dIa = self.lmbda_1 * self.p_a * E1 - self.mu * Ia
            dR = self.mu * (I + Ia)

            # put the values in the end of derivative
            derivative += [dS, dE1, dE2, dI, dIa, dR]

        return derivative


    def solution(self, u, t):
        n = len(t)
        n_reg = len(self.region)
        self.t = t
        self.S = np.zeros(n); self.E1 = np.zeros(n); self.E2 = np.zeros(n); self.I = np.zeros(n);
        self.Ia = np.zeros(n); self.R = np.zeros(n)

        SEIR_list = [u[:, i:i+6] for i in range(0, n_reg*6, 6)]

        for part, SEIR in zip(self.region, SEIR_list):
            part.set_SEIR_values(SEIR, t)
            self.S  += part.S
            self.E1 += part.E1
            self.E2 += part.E2
            self.I  += part.I
            self.Ia += part.Ia
            self.R  += part.R

    def plot(self):
        plt.xlabel('Time (days)')
        plt.ylabel('Population')
        plt.title(self.area_name)
        plt.plot(self.t, self.S, label='Susceptible')
        plt.plot(self.t, self.I, label='Infected Symptomatic')
        plt.plot(self.t, self.Ia, label='Infected Asymptomatic')
        plt.plot(self.t, self.R, label='Recovered')


if __name__ == '__main__':
    innlandet = RegionInteraction('Innlandet',S_0=371385, E2_0=0, \
                         lat=60.7945,long=11.0680)
    oslo = RegionInteraction('Oslo',S_0=693494,E2_0=100, \
                         lat=59.9,long=10.8)

    print(oslo.distance(innlandet))

    problem = ProblemInteraction([oslo,innlandet],'Norway_east', beta=0.5)
    print(problem.get_population())
    problem.set_initial_condition()
    print(problem.initial_condition) #non-nested list of length 12
    u = problem.initial_condition
    print(problem(u,0)) #list of length 12. Check that values make sense

    #when lines above work, add this code to solve a test problem:
    solver = SolverSEIR(problem,T=100,dt=1.0)
    solver.solve()
    problem.plot()
    plt.legend()
    plt.show()


"""
Drive Code:

0.10100809386285284
1064979
[693494, 0, 100, 0, 0, 0, 371385, 0, 0, 0, 0, 0]
[-62.49098896472576, 62.49098896472576, -50.0, 50.0, 0.0, 0.0, -30.250446610474285, 30.250446610474285, 0.0, 0.0, 0.0, 0.0]
"""
