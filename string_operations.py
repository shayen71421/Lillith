# String operations
# Taking string input from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Creating and concatenating strings
concatenated_str = str1 + " " + str2
print("Concatenated String:", concatenated_str)

# Accessing a substring using built-in functions
start_index = int(input("Enter the starting index for substring: "))
end_index = int(input("Enter the ending index for substring: "))
substring = concatenated_str[start_index:end_index]  # Extracting substring
print("Substring using built-in function:", substring)

# Accessing a substring without using built-in functions
substring_without_builtin = ""
for i in range(start_index, end_index):
    substring_without_builtin += concatenated_str[i]
print("Substring without using built-in functions:", substring_without_builtin)

# List operations
# Creating a list dynamically
dynamic_list = []
n = int(input("How many elements do you want to add to the list? "))

for _ in range(n):
    element = int(input("Enter a number: "))
    dynamic_list.append(element)  # Using built-in function to add elements

# Finding the largest value from the list using built-in function
largest_value = max(dynamic_list)
print("Largest value in the list (using built-in function):", largest_value)

# Finding the largest value from the list without using built-in function
if len(dynamic_list) > 0:
    largest_value_without_builtin = dynamic_list[0]
    for num in dynamic_list:
        if num > largest_value_without_builtin:
            largest_value_without_builtin = num
    print("Largest value in the list (without using built-in functions):", largest_value_without_builtin)
else:
    print("The list is empty.")
