# dictionary = a collection of {key:value} pairs
#              ordered and changeable, no duplicates

capitals = {"USA":"Washington D.C",
            "India":"New Delhi",
            "china":"Beijing",
            "Russia":"Moscow"} # craeting a dictionary

print(dir(capitals)) #shows what all u can do
print(help(capitals)) # gievs help on what to do

print(capitals.get("USA")) #prints the value of the key
#if the key doesnt exist then we get None as output which can be used as true or false in if statement

capitals.update({"Germany":"Berlin"}) #add new key amd value
print(capitals) #prints everything
capitals.update({"USA":"Detroit"}) #can be used to overwrite the value of a key
capitals.pop("China") #pops it out
capitals.popitem() #will pop out the last key and value
keys=capitals.keys() #stores the keys and this can be used for loops related to dictionaries
print(keys) 
for key in capitals.keys():
    print(key)
values = capitals.values() #same as .keys but for values
items = capitals.items() #makes the dictiomnary into a 2d tuple
for key,value in capitals.items():
    print(f"{key} : {value}")
capitals.clear() # will clear all data  