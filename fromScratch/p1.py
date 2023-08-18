# ...........................................................................

import math
import this

"""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those! 
"""
# ...........................................................................
# Different Data types

name = "Sam"
ageNum = 44
stringSen = "Hii World!"
intNum = 9
floatNum = 3.45
listArr = ["app", "web", "host"]
dictObj = {"name": "Zam", "age": 43}
isBool = True

print(name, ageNum, stringSen, intNum, floatNum, listArr, dictObj, isBool)

# ...........................................................................
# INPUT FROM USER

age_str = input("Please enter your age: ")
age = int(age_str)  # Convert the string to an integer
print("You are", age, "years old.")
# ...........................................................................
# loops
# For loop
for k in listArr:
    print(k)

# Using a while loop to repeat a block of code until a condition is met
count = 0
while count < 5:
    print(count)
    count += 1
# ...........................................................................
# Function


def greet(name):
    print("Hello, " + name + "!")


greet("Sam")
# .............................................................................
# Arguments and Return


def add(a, b):
    return a + b


print(add(3, 4))
# ...........................................................................
# Importing Modules
radius = 5
area = math.pi * radius ** 2
print("Area: ", area)
# ...........................................................................
# Lists

# Creating the list
listA = ["app", 3, 3.12, [1, 2, 3, 4], True, {"name": "Sam", "age": 22}]

# Accessing the list elements
print(listA[0])  # first Element
print(listA[-1])  # last Element

# Modifying the list elements
listA[1] = "Changed"   # Change the second element
print(listA)
listA.append(89)  # Add an element to the end
print(listA)

# Slicing Lists
print(listA[1:4])  # Get a sublist from index 1 to 3
print(listA[:2])    # Get the first two elements
# ...........................................................................
# Dictionaries

# Creating Dictionaries:

person = {"name": "Alice", "age": 25, "is_student": True}
print(person)

# Accessing Dictionary Values:

print(person["name"])  # Access value using key
print(person.get("age"))  # Access value using get() method

# Modifying Dictionaries:

person["age"] = 26  # Update value for the "age" key
print(person)
person["city"] = "New York"  # Add a new key-value pair
print(person)
# ...........................................................................

# Looping Through a List:

for b in listA:
    print(b)

# Looping Through a Dictionary:
for key, value in person.items():
    print(key, ":", value)

# ...........................................................................
# OOPs

# Defining a class
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"The {self.make} {self.model} is driving.")


# Creating Objects
my_car = Car("Toyota", "Camry")
my_car.drive()
# ...........................................................................

