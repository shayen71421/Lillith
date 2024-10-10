# Sum of N Natural Numbers
n = int(input("Enter a positive integer (n): "))
if n < 1:
    print("Please enter a positive integer.")
else:
    sum_n = (n * (n + 1)) // 2 # Using // for integer division ensures the result is an integer
    print("The sum of the first", n, "natural numbers is:", sum_n)
