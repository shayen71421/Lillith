#This random module gives us access to lots of methods involving random numbers
import random
# print(help(random)) displays everything u can do with it
print(random.randint(1,6)) #gives output as how a dice gives int output
low=1
high=100
print(random.randint(low,high))
print(random.random()) # gives a float random u cant give limit generates btwn 0 to 1
options = {"rocks","paper","scissors"} #tuple
print(random.choice(options)) #chooses a random from a list
cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
print(random.shuffle(cards)) #shuffles the list
