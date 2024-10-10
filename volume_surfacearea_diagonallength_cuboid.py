# Cube Calculations: Volume, Surface Area, and Diagonal Length
side_length = float(input("Enter the length of one side of the cube: "))
volume = side_length ** 3
surface_area = 6 * (side_length ** 2)
diagonal_length = (3 ** 0.5) * side_length
print("Volume of the cube:", volume)
print("Surface area of the cube:", surface_area)
print("Length of the diagonal of the cube:", diagonal_length)