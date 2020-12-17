# Problem 7.2. Chemical elements in a dictionary

#a)
elements_10 = {1: '-', 2: 'Helium', 3: 'Lithium', 4: 'Beryllium', 5: 'Boron', 6: 'Carbon', 7: 'Nitrogen', 8: '-',
9: 'Fluorine', 10: 'Neon'}

#adjusting the dictionary such that the keys 1 and 8 have their correct value
elements_10[1] = 'Hydrogen'
elements_10[8] = 'Oxygen'

# b)
elements_10_copy = elements_10.copy()
elements_10_copy.update({11: 'Sodium'})
print(elements_10)
print('\n')
elements_11 = elements_10
elements_11.update({11: 'Sodium'})
print(elements_10)

print('\n')
print("""
 The call to elements_10.copy() ensures that elements_10_copy is a copy
 of the original dictionary, and not a reference. Therefore, updating the
 elements_10_copy does not alter the original dictionary "element_10".

 On the other hand, setting: elements_11 = elements_10 alters the original
 dictionary. Thus, updating "elements_11" also alters the original dictionary,
 "element_10".
""")

"""
printed:
 The call to elements_10.copy() ensures that elements_10_copy is a copy
 of the original dictionary, and not a reference. Therefore, updating the
 elements_10_copy does not alter the original dictionary "element_10".

 On the other hand, setting: elements_11 = elements_10 alters the original
 dictionary. Thus, updating "elements_11" also alters the original dictionary,
 "element_10".
 """
