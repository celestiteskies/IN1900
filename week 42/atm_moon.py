# Problem 7.4. Use string operations to create a dictionary

#returns a dictionary with the name of the elements as keys
#the particle density as value(upper case).
def convert(l1st):
    with open(l1st, 'r') as infile:
        lunar = dict() # empty dictionary
        infile.readline() # skip the first line
        for line in infile:
            words = line.split(";")
            for j in range(len(words)):
                word = words[j].upper()
                w = word.split("-")
                w[1] = w[1].replace(",000","000")
                lunar[w[0].strip()] = w[1].strip()
        for k, v in lunar.items():
            lunar[k] = float(v)
    return lunar

lunar = convert('atm_moon.txt')
print(f"Dictionary(elements and particle density): \n{lunar}")

"""
printed:
Dictionary(elements and particle density):
{'HELIUM 4': 40000.0, 'NEON 20': 40000.0, 'HYDROGEN': 35000.0, 'ARGON 40': 30000.0, 'NEON 22': 5000.0, 'ARGON 36': 2000.0, 'METHANE': 1000.0, 'AMMONIA': 1000.0, 'CARBON DIOXIDE': 1000.0}
"""
