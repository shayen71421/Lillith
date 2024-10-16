# Multiplication Table of a Number

num = int(input("Enter a number: "))
count = int(input("How many multiples do you want to display? "))

if count < 1:
    print("Please enter a positive integer for the count.")
else:
    for i in range(1, count + 1):
        result = num * i
        print(num, "x", i, "=", result)

# The same logic using a while loop:
# i = 1
# while i <= count:
#     result = num * i
#     print(num, "x", i, "=", result)
#     i += 1
