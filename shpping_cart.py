# shopping cart program
foods = []
prices = []
total = 0
 
while True:
    food=input("Enter a food to buy(press q to quit): ")
    if food.lower() == "q" :
        break
    else:
        price = float(input(f"Enter the price of {food}:"))
        foods.append(food)
        prices.append(price)

print("_____YOUR CART_____")
for food in foods:
    print(food,end=" ") # prints in in one line
for price in prices:
    total += price
    print() # to print ot next line cuz we started a single line before
print(f"Your total price is : {total} rupees")