from math import exp

B = 50000    #carrying capacity
h = 24
c = 0.2
t_0 = 0
N_0 = 5000   #population

k= c/h

#First find C:
C = (B - N_0)/N_0*exp(-k*t_0)

t= 24

#find N:
def population(t):
    pop=B/(1+C*exp(-k*t))
    return (pop)

pop = population(t)

print (f"C is: {C}. The number of bacteria in the colony after 24 hours is: {pop}.")

"""C is: 9.0. The number of bacteria in the colony after 24 hours is: 5974.731585569669."""
