# if and else  a nd elif condition
age= int(input("Enter ur age: "))
if age>=18:
    print("okay")
elif age<0:# special staement for in btwn if and else
    print("not born")
else:
    print("not okay")

response=input("type Y or N: ")
if response == "Y":
  print("ok")
else:
    print("nah")
#can be used with boolean and others
x=10
y=5
print("hi" if x >5 else y)
result = x if x>y else y
