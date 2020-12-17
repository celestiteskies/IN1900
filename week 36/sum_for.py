#Problem 3.4. Errors in summation

s=0
M=3

for k in range(1,M+1):              # range should be (1,M+1), otherwise range is [0,1,2]
    s += 1/(2*k)**2                 # i should be replaced by k, otherwise 'k' is not defined
    print(f"k is:{k:2d}, s is: {s}") # we need a parenthesis in (2*k), otherwise only k is raised to the power of 2

#what the sum function does:
#1/4+1/16+1/36

""" What is printed in the terminal:
k is: 1, s is: 0.25
k is: 2, s is: 0.3125
k is: 3, s is: 0.3402777777777778
"""
