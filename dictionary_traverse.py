# dictionary and traverse
# Creating a dictionary from user input
student_info = {}

# Taking inputs for dictionary values
student_info["name"] = input("Enter student's name: ")
student_info["age"] = int(input("Enter student's age: "))
student_info["course"] = input("Enter student's course: ")
student_info["year"] = input("Enter student's year: ")

# Traversing through the dictionary (key-value pairs)
print("\nTraversing through the dictionary (Key-Value Pairs):")
for key, value in student_info.items():
    print(key, ":", value)

# Traversing through the dictionary (only keys)
print("\nTraversing through the dictionary (Only Keys):")
for key in student_info.keys():
    print(key)

# Traversing through the dictionary (only values)
print("\nTraversing through the dictionary (Only Values):")
for value in student_info.values():
    print(value)
