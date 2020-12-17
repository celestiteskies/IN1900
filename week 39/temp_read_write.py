# Problem 5.10. Read temperatures from two files

import numpy as np

# a)

def extract_data(filename):
    infile = open(filename, "r")
    infile.readline() # skip the first line
    y=[]
    strings_2=[]
    for line in infile:
        split = line.split()
        y.append(split)
    strings_2 = [item for elem in y for item in elem]
    fil = [float(item) for item in strings_2]
    infile.close()

    return fil

#call extract_data function
oct_1945 = extract_data("temp_oct_1945.txt")
oct_2014 = extract_data("temp_oct_2014.txt")

#make arrays
oct_1945 = np.copy(oct_1945)
oct_2014 = np.copy(oct_2014)

#compute average, maximum and mean
mean_1945 = np.mean(oct_1945)
max_1945 = np.max(oct_1945)
min_1945 = np.min(oct_1945)

mean_2014 = np.mean(oct_2014)
max_2014 = np.max(oct_2014)
min_2014 = np.min(oct_2014)

print(f"The average temperature for October 1945 is: {mean_1945:.3f}. The maximum temperature is: \
{max_1945} Celsius degrees and the minimum: {min_1945} Celsius degrees.")
print()
print(f"The average temperature for October 2014 is: {mean_2014:.3f}. The maximum temperature is: \
{max_2014} Celsius degrees and the minimum: {min_2014} Celsius degrees.")

# b)
lists=  []
def write_formatting(filename, list1, list2):
    a=list1.reshape(-1,1)
    b= list2.reshape(-1,1)
    lists = np.append(a, b, axis =1)
    outfile = open("temp_formatted.txt", "w")
    space = " "
    l1="oct_1945"
    l2="oct_2014"
    outfile.write(f" {l1}    {l2}" +"\n")
    for row in lists:
        for column in (row):
            outfile.write(f"{column:9.2f}")
        outfile.write("\n")
    outfile.close()

create=write_formatting("temp_formatted.txt", oct_1945, oct_2014)

"""
printed:
The average temperature for October 1945 is: 6.506. The maximum temperature is: 11.6 Celsius degrees and the minimum: 2.1 Celsius degrees.

The average temperature for October 2014 is: 8.855. The maximum temperature is: 13.6 Celsius degrees and the minimum: 2.3 Celsius degrees.
"""
