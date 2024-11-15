# function = A block of reusable code
#  (postional arguements)          place () after the function to call it

def display_invoice(username, amount, due_date):
   print(f"Hello {username}")
   print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Shayen", 42.50, "01/02")
display_invoice("Thomas", 100.99, "02/03")

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("shayen", "thomas")
print(full_name)