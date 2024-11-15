# keyword arguements = preceded by an identifier
#                      helps with readability
#                      order of arguements doesn't matter
#                      position arguements is always first before keyword arguements


def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title="Mr.", last="Thomas", first="Shayen")




for number in range(1, 11):
    print(number, end=" ")

print("1", "2", "3", "4", "5", sep="-")




def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)