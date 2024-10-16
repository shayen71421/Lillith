# Print N Natural Numbers up to (n-1) using for loop

n = int(input("Enter a positive integer: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    for i in range(1, n):
        print(i)

# The same logic using a while loop:
# i = 1
# while i < n:
#     print(i)
#     i += 1
