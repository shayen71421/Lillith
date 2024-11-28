import pandas as pd

file_path = input("Enter the full path to the marks.csv file: ")

try:
    df = pd.read_csv(file_path)
    df['Total'] = df[['PhyMarks', 'Chemistry Marks', 'Maths Marks']].sum(axis=1)
    print(df.head())
    df.to_csv('updated_marks.csv', index=False)
    print("Updated file saved as 'updated_marks.csv' in the same folder as the script.")
except FileNotFoundError:
    print("The file was not found. Please check the path and try again.")
