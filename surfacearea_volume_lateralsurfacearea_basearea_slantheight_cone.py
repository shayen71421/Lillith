# Surface Area, Volume, and Other Calculations for a Cone
radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))
slant_height = pow(pow(radius, 2) + pow(height, 2), 0.5)
lateral_surface_area = 3.14159 * radius * slant_height
base_area = 3.14159 * pow(radius, 2)
surface_area = lateral_surface_area + base_area
volume = (1 / 3) * 3.14159 * pow(radius, 2) * height
print("Slant height of the cone:", slant_height)
print("Lateral surface area of the cone:", lateral_surface_area)
print("Base area of the cone:", base_area)
print("Total surface area of the cone:", surface_area)
print("Volume of the cone:", volume)