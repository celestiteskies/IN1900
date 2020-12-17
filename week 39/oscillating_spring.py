# Problem 6.4. Oscillating spring

import numpy as np
import matplotlib.pyplot as plt

k = 4     #kg
γ = 0.15  #s^−1
m = 9     #kg
A = 0.3   #m
n = 101   #no of points

#a)
t_array = np.zeros(n)
y_array = np.zeros(n)
sp = 0    #starting point
ep = 25   #ending point
dx = (ep-sp)/(n-1) # x spacing in [1,10]

for i in range(0,n):
    t_array[i] = sp + i*dx
    y_array[i] = A*np.exp(-γ*t_array[i])*np.cos(np.sqrt(k/m)*t_array[i])
# print(f" t_array:")
# print (t_array)
# print()
# print(f" y_array:")
# print (y_array)

#storing the results in different name variables so we can plot t,y arrays from both exercises a) and b).
t_array1 = np.copy(t_array)
y_array1 = np.copy(y_array)

#b)
def y(t):
    return A*np.exp(-γ*t)*np.cos(np.sqrt(k/m)*t)

t_array = np.linspace(0, 25, n) # 101 intervals in [0,25]
y_array = y(t_array)
# print(f" t_array:")
# print (t_array)
# print()
# print(f" y_array:")
# print (y_array)

#c) plot
minimum = np.min(y_array)
maximum = np.max(y_array)

plt.plot(t_array, y_array, 'bo-', t_array1, y_array1, 'thistle')
plt.legend('ab)')
plt.xlabel("t (s)")
plt.ylabel("position (m)")
plt.axis([0, 25, -0.15 , 0.3])
plt.title("position of the rock against time")
plt.show()

print("Both plots are identical. We can confirm the arrays from exercise a) and b) give the same result.")
# #An alternative way to test if arrays are identical
# if (np.all(y_array) == np.all(y_array1)) and (np.all(t_array) == np.all(t_array1)):
#     print("y and t values identical!")
# else:
#     print("y and t values are not identical!")

"""
printed:

Both plots are identical. We can confirm the arrays from exercise a) and b) give the same result.
"""
