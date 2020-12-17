# Problem 9.4. Inheritance

#a)
class Mammal():
    def info(self):
        return "I have hair on my body"

    def identity_mammal(self):
        print ("I am a mammal")

#b)
#subclass of Mammal
class Primate(Mammal):
    def info(self):
        return super().info() + ", I have a large brain"

    def identity_primate(self): #equivalent to identity_mammal()
        print ("I am a primate")

#c)
#subclasses of Primate
class Human(Primate):
    def info(self):
        return super().info() + ", I have logic"

    def identity_human(self):
        print ("I am human")

class Ape(Primate):
    def info(self):
        return super().info() + ", I do not have tail"

    def identity_ape(self):
        print ("I am an ape")


John = Human(); Julius = Ape()

print("John")
print(John.info())
John.identity_mammal()
John.identity_primate()
John.identity_human()
# John.identity_ape()  #--->error
print()

print("Julius")
print(Julius.info())
Julius.identity_mammal()
Julius.identity_primate()
# Julius.identity_human()  #--->error
Julius.identity_ape()
print()

print("""Subclasses can leverage code from another base class.
Calling 'John.identity_ape()' causes en error since there isn't such method for the class human.
Respectively 'Julius.identity_human()' causes also en error.""")
print()

#d)
print("John")
print("---------------")
print(f"Mammal   {isinstance(John, Mammal)}")
print(f"Primate  {isinstance(John, Primate)}")
print(f"Human    {isinstance(John, Human)}")
print(f"Ape      {isinstance(John, Ape)}")
print()

print("Julius")
print("---------------")
print(f"Mammal   {isinstance(Julius, Mammal)}")
print(f"Primate  {isinstance(Julius, Primate)}")
print(f"Human    {isinstance(Julius, Human)}")
print(f"Ape      {isinstance(Julius, Ape)}")



"""
Drive code:

John
I have hair on my body, I have a large brain, I have logic
I am a mammal
I am a primate
I am human

Julius
I have hair on my body, I have a large brain, I do not have tail
I am a mammal
I am a primate
I am an ape

Subclasses can leverage code from another base class.
Calling 'John.identity_ape()' causes en error since there isn't such method for the class human.
Respectively 'Julius.identity_human()' causes also en error.

John
---------------
Mammal   True
Primate  True
Human    True
Ape      False

Julius
---------------
Mammal   True
Primate  True
Human    False
Ape      True
"""
