# ---------- main.py ----------
#print(help("module")) prints all the modules avialable
# print(help("math")) prints all the functions in a module
#import math
# from math import e   imports the needed one only
import math as m #sets up a custom name for modules
result = m.pi
result = m.square(3)
result = m.cube(3)
result = m.circumference(3)
result = m.area(3)

print(result)

# ---------- creating a module ----------
#create this in a file for example named erd.py then create another file in same folder and weite import erd
# then for example use erd.pi or erd.sqaure etc to use it
pi = 3.14159

def square(x):
   return x ** 2

def cube(x):
   return x ** 3

def circumference(radius):
   return 2 * pi * radius

def area(radius):
   return pi * radius ** 2