# Problem 1.4. Simulate Covid19 in Norway

import numpy as np
import matplotlib.pyplot as plt
from SEIR_interaction import *
from datetime import *

#a)
def Read_RegionInteraction(filename):
    with open(filename, 'r') as infile:

        #process/format information
        regions = []
        for line in infile:
            fylke_info = line.split(';')[1:]
            name = fylke_info.pop(0).strip()
            S_0, E2_0, lat, long = [float(info) for info in fylke_info]
            r = [S_0, E2_0, lat, long]

            #returns a list of RegionInteraction instances
            regions.append(RegionInteraction(name, S_0, E2_0, lat, long))
        infile.close()

    return regions


#b)
def covid19_Norway(beta, filename, num_days, dt):
    #read file and create list of RegionInteraction instances
    regions = Read_RegionInteraction(filename)

    #create problem, an instance of ProblemInteraction
    problem = ProblemInteraction(regions, 'Norway', beta)
    problem.set_initial_condition()

    #create the solver-call the method solve
    solver = SolverSEIR(problem, num_days, dt)
    solver.solve()

    #plotting
    fig = plt.figure(figsize=(9,12))
    index = 1
    for region in problem.region:
        plt.subplot(4,3,index)
        region.plot()
        index += 1
    plt.subplot(4,3,index)
    plt.subplots_adjust(hspace = 0.75, wspace=0.5)
    problem.plot()
    plt.legend(bbox_to_anchor=(1.05, 1.0, 0.3, 0.2), loc='upper left')
    fig.suptitle("Disease dynamics", fontsize=12)
    plt.show()

#task b): first plot
covid19_Norway(beta =0.5, filename='fylker.txt', num_days=500, dt=1.0)

print("""
b)

By examining the plot of the total cases(Norway) we can conclude that the approximate
peak for the I(Infected Symptomatic) category is 1.000.000.

Estimates from the early phase of the pandemic indicated that about 20% of
the infected cases would need hospital care, i.e 200.000.

5% of those would need a mechanical ventilator, i.e 10.000(estimate).
There are around 700 ventilators in Norwegian hospitals.

This means that the number of ventilators is extremely small comparing to the estimate.
There should roughly be 9.300 more ventilators to treat the respectively infected cases.

""")

#c)
#constants
r_e2 = 1.25
λ_2 = 0.5
r_ia = 0.1
μ = 0.2

def β_parameter(t):
    t0 = date(2020, 2, 15) #time zero
    t = t0 + timedelta(t)

    if t < date(2020, 3, 15):
        R = 4.0
    elif t < date(2020, 4, 21):
        R = 0.5
    elif t < date(2020, 5, 11):
        R = 0.4
    elif t < date(2020, 7, 1):
        R = 0.8
    elif t < date(2020, 8, 1):
        R = 0.9
    elif t < date(2020, 9, 1):
        R = 1.0
    else:
        R = 1.1

    β = R / (r_e2 / λ_2 + r_ia / μ + 1 / μ)

    return β

print("c)")
#second plot: β_parameter in the model
covid19_Norway(β_parameter, filename='fylker.txt', num_days=500, dt=1.0)

def β_experiment(t):
    t0 = date(2020, 10, 15) #time zero
    t = t0 + timedelta(t)

    if t < date(2020, 3, 15):
        R = 4.0
    elif t < date(2020, 4, 21):
        R = 0.5
    elif t < date(2020, 5, 11):
        R = 0.4
    elif t < date(2020, 7, 1):
        R = 0.8
    elif t < date(2020, 8, 1):
        R = 0.9
    elif t < date(2020, 9, 1):
        R = 4.0
    else:
        R = 1.1

    β = R / (r_e2 / λ_2 + r_ia / μ + 1 / μ)
    return β

#third plot: β_experiment in the model
covid19_Norway(β_experiment, filename='fylker.txt', num_days=500, dt=1.0)

print("""
If we assume R = 4.0 after September 1st, the nuber of Susceptible
decreases and the number of Recoverd increases in the time interval of days[0, 100].

The number of infected is very low and finally decreases.
""")


"""
Drive code:

(3 plots)

b)

By examining the plot of the total cases(Norway) we can conclude that the approximate
peak for the I(Infected Symptomatic) category is 1.000.000.

Estimates from the early phase of the pandemic indicated that about 20% of
the infected cases would need hospital care, i.e 200.000.

5% of those would need a mechanical ventilator, i.e 10.000(estimate).
There are around 700 ventilators in Norwegian hospitals.

This means that the number of ventilators is extremely small comparing to the estimate.
There should roughly be 9.300 more ventilators to treat the respectively infected cases.


c)

If we assume R = 4.0 after September 1st, the nuber of Susceptible
decreases and the number of Recoverd increases in the time interval of days[0, 100].

The number of infected is very low and finally decreases.

"""
