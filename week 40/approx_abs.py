# Problem 6.13. Approximate |x|

import numpy as np
import matplotlib.pyplot as plt

#function that approximates |x|
def abs_approx(x,N):
    index_set = range(N+1)
    Σ = np.zeros(len(index_set))
#     print(f"Exact: abs({x}) = {np.abs(x)}")
    for n in index_set[1:]:
        Σ = np.cos((2*n-1)*x)*(2*n-1)**(-2)
        Σ += Σ
    Σ = np.array(Σ)
    approx =  np.pi/2 - (4/np.pi)*Σ
    approx = np.array(approx)
#     print(f"x: {x}\nabs approximation: {approx}\nerror: {np.abs(approx-np.abs(x)):.5f}")
    return approx

N = 4
x_values = np.linspace(-np.pi, np.pi) #creating uniformly x values using default(50)
y_approx = []
y_real = []
for x in (x_values):
    y1 = abs_approx(x, N)
    y_approx.append(y1) #approximated values
    y2 = np.abs(x)
    y_real.append(y2)   #exact abs values

#turning into arrays
y_approx = np.array(y_approx)
y_real = np.array(y_real)

#compute min, max of y values
maximum = np.max(y_real)
# print(maximum)
minimum = np.min(y_real)
# print(minimum)

for N in range(1, N+1):
    plt.plot(x_values, abs_approx(x_values, N), label=f'N = {N}')
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.axis([-np.pi, np.pi, minimum, maximum])
    plt.title("f(x) = |x|")
    plt.show()

"""
(4 plots)
"""
