#....................................................................................

# Print area and circumference of the Circle 

import math

r=float(input("Enter the radius of Circle: "))
area = (math.pi)*r**2
print("Area: ", area)
circumference=2*math.pi*r
print("Circumference: ",circumference)

#....................................................................................
# Write a Python program that prints all even numbers from 1 to 20 using a loop.
for i in range(1,21):
  if(i%2==0):
    print(i)

#....................................................................................
# Write a Python function that calculates the factorial of a given number.

# def factorial(n):
#   if(n==0 or n==1):
#     return 1
#   return n*factorial(n-1)

# x=int(input("Enter number to calculate its Factorial: "))
# print("Factorial: ",factorial(x))

def factorial(n):
  result=1
  for i in range(1,n+1):
    result*=i
  return result

x=int(input("Enter number to calculate its Factorial: "))
print("Factorial: ",factorial(x))
#....................................................................................
# Write a Python program that takes a list of numbers as input from the user 
# and calculates the sum and average of the numbers.

x=input("Enter list of numbers seperated by space: ")
nums=list(map(int,x.split()))
def cal(nums):
  sum=0
  for i in nums:
    sum+=i
  print(float(sum/len(nums)))
cal(nums)
#....................................................................................

#  Word Frequency Counter
# Write a Python program that takes a sentence as input 
# and counts the frequency of each word. Use a dictionary to store the word frequencies.

A=input("Enter the words seperated by spaces ")
listA=list(map(str,A.split()))
def solve(arr):
  x={}
  for i in arr:
    if(i in x):
      x[i]+=1
    else:
      x[i]=1
  # Print the word frequencies
  print("Word Frequencies:")
  for a,b in x.items():
    print(f"{a}: {b}")

solve(listA)

#....................................................................................
# Pattern Printing

def pattern(n):
  for i in range(1,n+1):
    for j in range(i):
      print("*",end="")
    print()

pattern(5) 
#....................................................................................

# Create a Python class called Rectangle that represents a rectangle. 
class Rectangle:
  def __init__(self, length, width):
    self.length=length
    self.width=width
        # Initialize attributes here

  def area(self):
        # Calculate and return the area
      return self.length*self.width

  def perimeter(self):
        # Calculate and return the perimeter
      return 2*(self.length+self.width)

myRec=Rectangle(3,4)
print(myRec.area())
print(myRec.perimeter())