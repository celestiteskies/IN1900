# Problem 5.7. Read isotope file

def extract_data(Oxygen):
    infile = open("Oxygen.txt", "r")
    infile.readline() # skip the first line
    isotope = []
    weight = [] #[g/mol]
    abundance = []
    for line in infile:
        words = line.split() #words[0] + words[1]: isotope, words[2]: weight, words[3]: abundance
        isotope.append(words[0] + words[1])
        weight.append(float(words[2]))
        abundance.append(float(words[3]))
    infile.close()
    return isotope, weight, abundance

isotope, weight, abundance = extract_data("Oxygen.txt")

def Molar(isotope, weight, abundance):
    """
    Calculates the molar mass, M, of oxygen by summing over all its isotopes M = weight_i*abundance_i,
    of the i-th isotope.
    """
    M = 0
    for i in range(len(isotope)):
       M += weight[i]*abundance[i]
    return M

M= Molar(isotope, weight, abundance)
print(f"The molar mass of Oxygen is: {M:.4f} g/mol.")


"""
printed on terminal:
The molar mass of Oxygen is: 15.9994 g/mol.
"""
