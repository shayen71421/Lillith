#List comprehension = A concise way to create lists in Python
#                     Compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]
print(doubles)
print(triples)
print(squares)
fruits = ["apple", "orange", "banana", "coconut"]
print(fruits)
uppercase_words = [fruit.upper() for fruit in fruits]
print(uppercase_words)
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)
numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_numbers = [x for x in numbers if x >= 0]
print(positive_numbers)
negative_numbers = [x for x in numbers if x < 0]
print(negative_numbers)
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
odd_numbers = [x for x in numbers if x % 2 == 1]
print(odd_numbers)
grades = [85, 42, 79, 90, 56, 61, 30]
print(grades)
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)