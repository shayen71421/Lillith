# Fibonacci Series up to Nth term without recursion

n = int(input("Enter the number of terms: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    a, b = 0, 1
    print("Fibonacci series for", n, "terms:")
    
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# The same logic to print Fibonacci series up to a value n:
# n = int(input("Enter a positive integer: "))
# a, b = 0, 1
# print("Fibonacci series up to", n, ":")
# while a <= n:
#     print(a, end=" ")
#     a, b = b, a + b
