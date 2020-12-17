#Problem 3.11. Molar Mass of Alkanes

MC = 12.011  #molar mass of Carbon in g/mol
MH = 1.0079  #the molar mass of Hydrogen in g/mol

#compute and print the molar mass of the alkanes
for n in range(2,10):
    m = (2*n +2)
    mol = n*MC + m*MH
    if m<= 8: #(if statement in order to align the printed numbers)
        print(f"M(C{n}H{m}) {mol:8.3f} g/mol")
    else:
        print(f"M(C{n}H{m}) {mol:7.3f} g/mol")

"""Printed in terminal:
M(C2H6)   30.069 g/mol
M(C3H8)   44.096 g/mol
M(C4H10)  58.123 g/mol
M(C5H12)  72.150 g/mol
M(C6H14)  86.177 g/mol
M(C7H16) 100.203 g/mol
M(C8H18) 114.230 g/mol
M(C9H20) 128.257 g/mol
"""
