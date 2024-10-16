# Sum of N Natural Numbers
n = int(input("Enter a positive integer (n): "))
if n < 1:
    print("Please enter a positive integer.")
else:
    sum_n = (n * (n + 1)) // 2 # Using // for integer division ensures the result is an integer
    print("The sum of the first", n, "natural numbers is:", sum_n)
    
"""
# Sum of N Natural Numbers using for loop

n = int(input("Enter a positive integer: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    sum_n = 0
    for i in range(1, n + 1):
        sum_n += i
    print("The sum of the first", n, "natural numbers is:", sum_n)

"""
# The same logic using a while loop:
# sum_n = 0
# i = 1
# while i <= n:
#     sum_n += i
#     i += 1
# print("The sum of the first", n, "natural numbers is:", sum_n)
