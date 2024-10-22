# Fibonacci Series using Recursion and writing to a file

# Function to calculate Nth Fibonacci number using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Main code to print Nth Fibonacci number and write Fibonacci series to a file
n = int(input("Enter the number of terms: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    # Open a file to write the Fibonacci series
    with open("fibonacci_series.txt", "w") as file:
        a, b = 0, 1
        print(f"Fibonacci series for {n} terms:", file=file)
        
        # Writing the Fibonacci series up to Nth term in the file
        for i in range(n):
            file.write(str(a) + " ")
            a, b = b, a + b

    # Printing the Nth Fibonacci number using recursion
    nth_fibonacci = fibonacci(n - 1)
    print(f"The {n}th Fibonacci number is: {nth_fibonacci}")

# The same logic to print Fibonacci series up to a value N (commented):
# n = int(input("Enter a positive integer: "))
# a, b = 0, 1
# with open("fibonacci_series.txt", "w") as file:
#     print(f"Fibonacci series up to {n}:", file=file)
#     while a <= n:
#         file.write(str(a) + " ")
#         a, b = b, a + b

# To print Fibonacci series using recursion for each term:
# def fibonacci_series_rec(n, a=0, b=1):
#     if n == 0:
#         return
#     else:
#         print(a, end=" ")
#         fibonacci_series_rec(n - 1, b, a + b)
# fibonacci_series_rec(n)

