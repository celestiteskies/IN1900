# Problem A.2. Solve a difference equation numerically

n = 15
χ0 = χ1 = 1
Σ = 0
count = 0
print("Fibonacci sequence: 15 first elements")
print("   χ   element")
while(count <= n-1):
    count += 1
    χ0 = χ1
    χ1 = Σ
    Σ = χ0 + χ1
    print(f"{count:4}: {Σ:3}")

"""
printed:

Fibonacci sequence: 15 first elements
   χ   element
   1:   1
   2:   1
   3:   2
   4:   3
   5:   5
   6:   8
   7:  13
   8:  21
   9:  34
  10:  55
  11:  89
  12: 144
  13: 233
  14: 377
  15: 610
"""
