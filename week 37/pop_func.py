# Problem 4.1

from math import exp
import numpy as np

B = 50000    #carrying capacity
k = 0.2
C = 9.0

def population(t,k,B,C):
    pop=B/(1+C*exp(-k*t))
    return(pop)

n=12
t=[]
N=[]

#13 uniformly spaced t values throughout the interval [0, 48]
t_values = np.linspace(0, 48, num=13)
# print(t_values)

#computes and stores t and N values in two lists t and N
for i in t_values:
    t.append(i)
#     print(t)
    N.append(population(i,k,B,C))
#     print (N)

#Storing the two lists in a new nested list tN1
tN1 = []
tN1.append(t)
tN1.append(N)
#print (tN1)
#print (f" The nested list tN1: {tN1} \n List tN1[0] containing t-values: {tN1[0]} \n List tN[1] containing N-values: {tN1[1]}")

#Write out a table with t and N values in two columns by looping over the data in the tN1 list.
print (" t ", " N")
for a,b in zip(tN1[0], tN1[1]):
    print(f"{int(a):2} {int(b):6}")


""" Printed it terminal:
 t   N
 0   5000
 4   9912
 8  17748
12  27526
16  36580
20  42924
24  46551
28  48389
32  49263
36  49666
40  49849
44  49932
48  49969
"""
