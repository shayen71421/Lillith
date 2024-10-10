# Area and Perimeter of a Triangle
side_a = float(input("Enter the length of side A: "))
side_b = float(input("Enter the length of side B: "))
side_c = float(input("Enter the length of side C: "))
s = (side_a + side_b + side_c) / 2
area = pow(s * (s - side_a) * (s - side_b) * (s - side_c), 0.5)
perimeter = side_a + side_b + side_c
print("Area of the triangle:", area)
print("Perimeter of the triangle:", perimeter)