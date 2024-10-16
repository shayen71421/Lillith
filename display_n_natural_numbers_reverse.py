# Print N Natural Numbers in Reverse Order using for loop

n = int(input("Enter a positive integer: "))
n -=1
if n < 1:
    print("Please enter a positive integer.")
else:
    for i in range(n, 0, -1):
        print(i)

# The same logic using a while loop:
# while n > 0:
#     print(n)
#     n -= 1
