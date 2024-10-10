#condional operator = a one line shortcut for the if else statement(ternary operator)
# print or assign one of the two values based on  a condition
# X if condtion else Y
num=5
a=10
b=7
print("Positive" if num > 0 else "Negative" )
print("Odd" if num%2!=0 else "Even")
max_num = a if a>b else b
min_num= a if a<b else b
