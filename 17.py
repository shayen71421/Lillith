# collection = single "variable" used to store multiple values
# list = [] ordered and changeable.Duplicates OK
# set = {} unordered and immutable,but add/remove Ok.No duplicates
# Tuple = () ordered and unchangeable.Duplicates OK.Faster
 
fruits = ["apple","orange","banana","coconut"]
print(fruits[0]) #prints the data at that index
print(fruits[0:3]) # prints 0 to 3
print(fruits[::2]) #prints every secind element
print(fruits[::-1]) # prints reverse
print(fruits[::-2]) # prints evry 2nd elemet but in reverse

for fruit in fruits:#naming convention like list = cars then x= car
    print(fruit)

print(dir(fruits)) # prints all things which can be done with this
print(help(fruits)) # gives a description of what is capable with a list
print(len(fruits)) # finds length
print("apple" in fruits) # finds and returns boolean
fruits.append("pineapple") #to add elemet to the end of the list
fruits.remove("apple") # to remove data form list
fruits.insert(0,"jackfruit") # used to insert data at a specific index
fruits.sort() # to sort a list
fruits.reverse() # in reverse order
fruits.index("apple") # to find index of a data
fruits.count("apple") # counts how many times the data is repeated
fruits.clear() #to clear the list
'''
 to make a set change [] to {} rest r same
 can't have duplicates
 wont have a order and wont be in the order we gave input
 most methods r same and everything works for a set as same as a list
 can print using index cuz they r unordered
 .add("data") used to add element
 .remove("data") to remove elemet
 .pop() pops on eout randomly
 help funtion is also available


help funtion is there so can be done accordingly
'''