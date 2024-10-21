# Factorial of a Number using Recursion

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Enter a non-negative integer: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print("The factorial of", num, "is:", result)

# Factorial of a Number using iteration
# num = int(input("Enter a non-negative integer: "))
# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial *= i
#     print("The factorial of", num, "is:", factorial)
#     # can find the factorial up to 1558
