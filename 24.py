#  Arbitrary arguements
# *args(args is a naming convention,star is imp)=multiple non key arguements,stored as tuple
# **kwargs(naming convention) = multiple key arguements,stored as dic

# ----- *ARGS Example 1 -----

def add(*nums):
   total = 0
   for num in nums:
       total += num
   return total

print(add(1, 2, 3, 4))

# ----- *ARGS Example 2 -----

def display_name(*args):
   print(f"Hello", end=" ")
   for arg in args:
       print(arg, end=" ")

display_name("Ser.", "Antony, The 3rd", "of", "House Kalium")

# ----- **KWARGS -----
def print_address(**kwargs):
    for value in kwargs.values():
        print(value, end=" ")

print_address(street="123 Fake St.",
              pobox="P.O Box 777",
              city="fake city",
              state="fake state",
              zip="00000")

# ----- EXERCISE -----
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants",
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")