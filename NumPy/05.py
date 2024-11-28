import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

phy_max = int(input("Enter the total marks for Physics: "))
chem_max = int(input("Enter the total marks for Chemistry: "))
maths_max = int(input("Enter the total marks for Maths: "))

students = int(input("Enter the number of students: "))
data = {'Student Name': [], 'PhyMarks': [], 'Chemistry Marks': [], 'Maths Marks': []}

for _ in range(students):
    name = input("Enter student name: ")
    phy_marks = int(input(f"Enter Physics marks for {name}: "))
    chem_marks = int(input(f"Enter Chemistry marks for {name}: "))
    maths_marks = int(input(f"Enter Maths marks for {name}: "))
    
    data['Student Name'].append(name)
    data['PhyMarks'].append(phy_marks)
    data['Chemistry Marks'].append(chem_marks)
    data['Maths Marks'].append(maths_marks)

df = pd.DataFrame(data)
df.to_csv('student_marks.csv', index=False)

df['Total'] = df[['PhyMarks', 'Chemistry Marks', 'Maths Marks']].sum(axis=1)

print(df.head())

plt.figure(figsize=(10, 6))
plt.bar(df['Student Name'], df['Total'], color='skyblue')
plt.xlabel('Student Name')
plt.ylabel('Total Marks')
plt.title('Total Marks of Students')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
