# Problem 7.6. Saving information in a nested dictionary

#a)
def read_person_data(file):
    return {line.split()[0].strip(","):{'Age':int(line.split()[1].strip(",")),'Gender':line.split()[2].strip(",")} for line in open(file)}

people = read_person_data('people.txt')

# or:
# def read_person_data(filename):
#     with open(filename, "r") as f:
#         d = {}
#         for line in f:
#             data = line.rstrip().split(",")
#             d.update({data[0]: {"Age": data[1].strip(), "Gender": data[2].strip()}})
#     return d

#b)
def write_person_data(data_dict, filename):
    with open(filename,'w') as data:
        for key in data_dict:
            data.write(f"{key}, {data_dict[key]['Age']}, {data_dict[key]['Gender']} \n")

people.update({"Celine": {"Age": 11, "Gender": "Female"}})
write_person_data(people, "new_people_dict.txt")

"""
(writes a txt file: "new_people_dict.txt")
"""
