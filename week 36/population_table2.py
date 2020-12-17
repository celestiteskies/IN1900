#Problem 3.8. Nested list

from math import exp
import numpy as np

B = 50000    #carrying capacity
h = 24
c = 0.2
C = 9.0

k= c/h
t= 24

#function that calculates the growth of a population (N)
def population(t):
    pop=B/(1+C*exp(-k*t))
    return (pop)

# Task a)
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

#Storing the two lists in a new nested list tN1
tN1 = []
tN1.append(t)
tN1.append(N)
#print (f" The nested list tN1: {tN1} \n List tN1[0] containing t-values: {tN1[0]} \n List tN[1] containing N-values: {tN1[1]}")

#t and N values in two columns
print ("t and N values in two columns(by looping over the data in the tN1 list):")
for a,b in zip(tN1[0], tN1[1]):
    print(int(a), int(b))

print()
#make integers
tN1 = np.array(tN1,dtype=int)
# print (tN1)

#tN2[i] contains the i-th element of both the t-list and the N-list
print ("tN2 nested list:")
tN2 = [[tN1[j][i] for j in range(len(tN1))] for i in range(len(tN1[0]))]

for r in tN2:
   print(r)

"""Printed in terminal:
0 5000
4 5152
8 5308
12 5468
16 5632
20 5801
24 5974
28 6152
32 6334
36 6521
40 6712
44 6908
48 7109

tN2 nested list:
[0, 5000]
[4, 5152]
[8, 5308]
[12, 5468]
[16, 5632]
[20, 5801]
[24, 5974]
[28, 6152]
[32, 6334]
[36, 6521]
[40, 6712]
[44, 6908]
[48, 7109]
"""
