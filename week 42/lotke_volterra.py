# Problem A.6. Lotka-Volterra two species model

import numpy as np
import matplotlib.pyplot as plt

#constant values
α = 0.04     #natural growth rate of rabbits in the absence of predation
b = 0.1      #natural death rate of foxes in the absence of food (rabbits)
c = 0.005    #death rate per encounter of rabbits due to predation
e = 0.2      #efficiency of turning predated rabbits into foxes.
n = 500      #number of weeks

#initial values
r0 = 100     #initial number of rabbits
f0 = 20      #initial number of foxes
t0 = 0       #time

# create empty arrays to store populations
r = np.zeros(n)
f = x = np.zeros(n)

# initialize populations
r[0] = r0
f[0] = f0

# calculate new values for time(t), rabbits(r) and foxes(f)
t = np.linspace(t0,n,n)

for i in range(n)[:-1]:
    r[i+1] = r[i] + α*r[i] - c*r[i]*f[i]
    f[i+1]= f[i] + e*c*r[i]*f[i] - b*f[i]

plt.plot(t, r, 'r', t, f ,'b', linewidth = 2) 
plt.xlabel('time')
plt.legend(['rabbits', 'foxes'])
plt.ylabel('population')
plt.show()

"""
(plot)
"""
