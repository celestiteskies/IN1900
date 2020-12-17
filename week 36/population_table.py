#The code starts with parts from problem 2.3(Population growth)
#and ends up to the tasks of problem 3.7(Table showing population growth)

from math import exp
import numpy as np

B = 50000    #carrying capacity
h = 24
c = 0.2
t_0 = 0
N_0 = 5000   #initial population for problem 2.3

k= c/h

#First find C:
C = (B - N_0)/N_0*exp(-k*t_0)

t= 24

#function that calculates the growth of a population (N)
def population(t):
    pop=B/(1+C*exp(-k*t))
    return (pop)

# pop = population(t)
# print(pop)

n=12
t=[]
N=[]

#13 uniformly spaced t values throughout the interval [0, 48]
t_values = np.linspace(0, 48, num=13)
#print(t_values)

#computes and stores t and N values in two lists t and N
for i in t_values:
    t.append(i)
#     print(t)
    N.append(population(i))
#     print (N)

#traverses the lists with a separate for loop
#and writes out a table of t and N values
print ("  t  ", "   N")
x=[]
y=[]
for x, y in zip(t, N):
    print (f"{x:5.1f} {y:9.3f}")

""" Printed on the terminal screen:
  t      N
  0.0  5000.000
  4.0  5152.013
  8.0  5308.102
 12.0  5468.344
 16.0  5632.813
 20.0  5801.584
 24.0  5974.732
 28.0  6152.327
 32.0  6334.442
 36.0  6521.146
 40.0  6712.507
 44.0  6908.591
 48.0  7109.463
"""
