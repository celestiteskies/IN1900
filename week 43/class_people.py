# Problem 8.1. Saving information in a class

class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def name_change(self, new_name):
        self.name = new_name

    def age_change(self, new_age):
        self.age = new_age

    def gender_change(self, new_gender):
        self.gender = new_gender

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}, gender: {self.gender}"

#information of the instance before changing
person = Person("John", "32", "male")
print(f"Information before changing: {person}")

#after changing
person.name_change("Simone"); person.age_change("16"); person.gender_change("female")
print(f"Information after changing: {person}")

"""
printed:

Information before changing: Name: John, age: 32, gender: male
Information after changing: Name: Simone, age: 16, gender: female
"""
