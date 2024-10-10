# Find the Greatest of Two Numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    greatest = num1
    print("The greatest number is:", greatest)
elif num2 > num1:
    greatest = num2
    print("The greatest number is:", greatest)
else:
    print("Both numbers are equal.")