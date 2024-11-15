# Match-case statement (switch): An alternative to using many 'elif' statements
#                                                          Execute some code if a value matches a 'case'
#                                                          Benefits: cleaner and syntax is more readable

def day_of_week(day0):
    if day0==1:
        return "Sunday"
    elif day0==2:
        return "Monday"
    elif day0==3:
        return "Tuesday"
    elif day0==4:
        return "Wednesday"
    elif day0==5:
        return "Thurday"
    elif day0==6:
        return "Friday"
    elif day0==7:
        return "Saturday"
    else:
        return "an Invalid input"
print("It is ",day_of_week(int(input("Enter the day number: "))))
def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return "It is a weekend" #True or False can also be used
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "It is not a weekend"
        case _:
            return "Invalid input"

print(is_weekend(day_of_week(int(input("Enter the day number: ")))))

