## Topic 1: Introduction to Python

Python is known for its simple and readable syntax. It's a great language for beginners.

### Python's Philosophy and Strengths:
---

Python is known for its simplicity, readability, and versatility. 
It follows ***the Zen of Python***, which is a set of guiding principles for writing computer programs in the Python language. You can access these guiding principles by typing **import this** in a Python interpreter.

Python's strengths include 
    - its clean and easy-to-understand syntax, which makes it a great choice for beginners. 
    - It also has a vast standard library and a large community, which means you have access to a wide range of tools, modules, and resources.

---
### No need for explicit type declarations.
---

```
name="Sam"
age=44
stringSen="Hii World!"
intNum=9
floatNum=3.45
listArr=["app","web","host"]
dictObj={"name":"Zam", "age":43}
isBool=True
```
---
### How to take INPUT FROM USER
---
The input is always treated as a **String**. So, if you need to work with other data types, you'll need to explicitly convert the input using appropriate conversion functions

```
age_str = input("Please enter your age: ")
age = int(age_str)  # Convert the string to an integer
print("You are", age, "years old.")
```
---
## Topic 2: Control Flow.

### Conditional Statements (if, elif, else):
---
Conditional statements allow you to make decisions in your code based on certain conditions.

```
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

```

---
### Loops: for Loops and while Loops:
---

Loops are used to repeatedly execute a block of code. Python provides two main types of loops: for loops and while loops.

```
# Using a for loop to iterate over a sequence

listArr=["app","web","host"]
for k in listArr:
    print(k)

# Using a while loop to repeat a block of code until a condition is met
count = 0
while count < 5:
    print(count)
    count += 1

```
---

### Indentation and Code Blocks:
---

Unlike many other programming languages, Python uses indentation (whitespace at the beginning of lines) to indicate code blocks. This means that indentation is crucial for structuring your code correctly. A consistent level of indentation is required for code within the same block.

---
## Topic 3: Functions and Modules

### Functions:
---

Functions are blocks of code that perform a specific task. They allow you to organize your code into reusable chunks. In Python, you define a function using the **def** keyword.

```
def greet(name):
    print("Hello, " + name + "!")

greet("Sam")
```
---
### Arguments and Return Values:
---

Functions can take input values called **arguments** and can also return values using the **return** keyword.

```
def add(a, b):
    return a + b

print(add(3,4))
```
---
### Importing Modules:
---
Modules are collections of functions, classes, and variables that are stored in separate files. Python provides a rich standard library, and you can also create your own modules.

```
import math
radius = 5
area = math.pi * radius ** 2

```
---

## Topic 4: Lists and Dictionaries

### Lists
---
A list is a collection of items in a specific order. Lists are versatile and can contain elements of different types, such as integers, strings, and even other lists.

```
# Creating
listA=["app",3,3.12,[1,2,3,4],True,{"name":"Sam","age":22}]

# Accessing the list elements
print(listA[0]) # first Element
print(listA[-1]) # last Element

# Modifying the list elements
listA[1]="Changed"   # Change the second element
print(listA)  
listA.append(89)  # Add an element to the end
print(listA)  

# Slicing Lists

print(listA[1:4])  # Get a sublist from index 1 to 3
print(listA[:2])    # Get the first two elements

```
---

### Dictionaries
---
A dictionary is a collection of key-value pairs. Each key is associated with a value, and you can use keys to access the corresponding values efficiently.

```
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

```
---
### Looping Through Lists and Dictionaries
---
You can use loops to iterate through the elements of a list or the key-value pairs of a dictionary.

```
# Looping Through a List:

for b in listA:
    print(b)

# Looping Through a Dictionary:
for key, value in person.items():
    print(key, ":", value)
```
---
**NOTE:** When iterating through the dictionary in the last loop, it's better to use different variable names for the key and value.
This makes the code more readable and avoids overwriting the dictionary values.

---

## Topic 5: Object-Oriented Programming (OOP)

### Object-Oriented Programming
---
Object-Oriented Programming is a programming paradigm that focuses on organizing code into objects, which are instances of classes. OOP provides a way to model real-world entities and their interactions in a more structured and modular manner.

### Classes and Objects
---
Class: A class is a blueprint for creating objects. It defines the properties (attributes) and behaviors (methods) that the objects of that class will have.

Object: An object is an instance of a class. It represents a specific entity with its own unique data and behavior.

---

```
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
```
---
### Constructor (```__init__```)
---
The ```__init__``` method is a special method called the **constructor**. It initializes the object's attributes when an object is created.

### Methods and Attributes
---
Methods: Functions defined within a class that define behaviors of the objects.

Attributes: Variables that store data for each object.

### Encapsulation, Inheritance, Polymorphism
---
OOP concepts include:

Encapsulation: Bundling data and methods that operate on the data into a single unit (class).

Inheritance: Creating a new class by inheriting attributes and methods from an existing class. It promotes code reusability.

Polymorphism: The ability of different classes to be treated as instances of the same class through inheritance.

---
### Bank Account Class
--- 
```
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

```
--- 
**Important**: method overloading, operator overloading, abstract classes