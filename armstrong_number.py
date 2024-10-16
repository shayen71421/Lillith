# Check if a Number is an Armstrong Number

num = int(input("Enter a number: "))
original_num = num
sum = 0
power = 0

# Calculate the number of digits (power)
temp = num
while temp > 0:
    temp //= 10
    power += 1

# Calculate the sum of the digits raised to the power
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** power
    temp //= 10

# Check if the sum equals the original number
if sum == original_num:
    print(original_num, "is an Armstrong number.")
else:
    print(original_num, "is not an Armstrong number.")

# The same logic using a for loop:
# original_num = num
# power = len(str(num))  # Calculate the number of digits
# sum = 0
# for digit in str(num):
#     sum += int(digit) ** power
# if sum == original_num:
#     print(original_num, "is an Armstrong number.")
# else:
#     print(original_num, "is not an Armstrong number.")
