#Problem 3.5. Sum as a while loop

s=0
M=3
k=1

while k >=1 and k <= M:
    s += 1/(2*k)**2
    print(f"k is:{k:2d}, s is:{s}")
    k= k+1

""" What is printed:
k is: 1, s is:0.25
k is: 2, s is:0.3125
k is: 3, s is:0.3402777777777778
"""
