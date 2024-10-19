# Palindrome

num = int(input("Enter a number: "))
original_num = num
reversed_num = 0

# Reverse the number using a while loop
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

# Check if the reversed number is equal to the original number
if original_num == reversed_num:
    print(original_num, "is a palindrome.")
else:
    print(original_num, "is not a palindrome.")

# The same logic using a for loop:
# num_str = str(original_num)
# reversed_num_str = num_str[::-1]  # Reverse the string
# if num_str == reversed_num_str:
#     print(original_num, "is a palindrome.")
# else:
#     print(original_num, "is not a palindrome.")
