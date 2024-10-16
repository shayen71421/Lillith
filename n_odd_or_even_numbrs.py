# Print odd or even numbers up to n based on user choice

n = int(input("Enter a positive integer: "))
choice = int(input("Enter 1 for odd numbers, 2 for even numbers: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    if choice == 1:
        i = 1
        print("Odd numbers up to", n, ":")
        while i < n:
            print(i)
            i += 2
    elif choice == 2:
        i = 2
        print("Even numbers up to", n, ":")
        while i < n:
            print(i)
            i += 2
    else:
        print("Invalid choice. Please enter 1 for odd or 2 for even.")
