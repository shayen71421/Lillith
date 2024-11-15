"""
Deafault arguements = A default value for certain parameters.
                      default is used when that arguement is omitted
                      makes your functions more flexible
                      reduces umber of arguements
                      1.postional 2.default 3.keyword 4.arbitrary                    
"""
# default arguements = setting default values to arguements

def net_price(list_price, discount=0, tax=0.05):
   return list_price * (1 - discount) * (1 - tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))



import time
def count(end, start=0): 
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(10)
count(30, 15)