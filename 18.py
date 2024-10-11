# 2D lists= list jmad eof lists

fruits =     ["apple","orange","banana","coconut"]
vegetables = ["celery","carrots","potatoes"]
meats =      ["chicken","fish","turkey"]

groceries = [fruits,vegetables,meats] # cerated a 2D list
print(groceries) # prints all of the lists
print(groceries[0]) # prints the 0th list
print(groceries[0][0]) #peints the 0th element of 0th list
# u can also directly add data into a 2D list instead of making several 1D lists
# use nested loops to iterate through a 2D list
for grocery in groceries:
    for item in grocery:
     print(item,end= "")
print()
# this can be done with tuples tooo
# u can also make a 2d tuples with sets tooo     