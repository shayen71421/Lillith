# Check if a number is a two-digit number and if it is odd or even
num = int(input("Enter a number: "))
if (num >= 10 and num < 100) or (num <= -10 and num > -100):
    if num % 2 == 0:
        print("The number is a two-digit even number.")
    else:
        print("The number is a two-digit odd number.")
else:
    print("The number is not a two-digit number.")