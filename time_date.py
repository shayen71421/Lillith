#Date and Time in Various Formats

from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format 1: "Thu Jul 11 10:26:23 IST 2024"
formatted1 = now.strftime("%a %b %d %H:%M:%S IST %Y")
print("Formatted date and time (Format 1):", formatted1)

# Format 2: "2024-07-11 10:26:23"
formatted2 = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time (Format 2):", formatted2)

# Format 3: "11 July 2024, 10:26:23"
formatted3 = now.strftime("%d %B %Y, %H:%M:%S")
print("Formatted date and time (Format 3):", formatted3)

# Format 4: "July 11, 2024"
formatted4 = now.strftime("%B %d, %Y")
print("Formatted date and time (Format 4):", formatted4)

# Format 5: "10:26:23"
formatted5 = now.strftime("%H:%M:%S")
print("Formatted date and time (Format 5):", formatted5)
