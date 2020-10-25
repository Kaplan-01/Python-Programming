# Calender.
import calendar

# Print month
print(calendar.month(2020,10))

# Print year
print(calendar.calendar(2021))


# Leap Year

year = int(input("Insert a year: "))

if year % 4 == 0:
    print("Lead year.")
else: 
    print("Normal year.")