# The following list comprehension exercises will make use of the 
# defined Human class. 
from math import sqrt
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

    def modifyHuman(self):
        self.name = self.name.upper()
        self.age += 5
        return self

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [getattr(human, "name") for human in humans if getattr(human, "name")[0] == 'D']
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [getattr(human, "name") for human in humans if getattr(human, "name")[-1] == 'e']
print(b)
# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = [getattr(human, "name") for human in humans if ord(getattr(human, "name")[0]) >= ord('C') and ord(getattr(human, "name")[0]) <= ord('G')]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [getattr(human, "age") + 10 for human in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [getattr(human, "name") + '-' + str(getattr(human, "age")) for human in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(getattr(human, "name"), getattr(human, "age")) for human in humans if getattr(human, "age") >= 27 and getattr(human, "age") <= 32]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.

#I need to return a modified human object in each iteration
#Without mutating t he original
print("All names uppercase:")
g = [Human(human.name.upper(), human.age + 5) for human in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(getattr(human, "age")) for human in humans]
print(h)