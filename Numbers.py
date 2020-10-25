# Super simple exercise about numbers.

# Positive and negative numbers. 

num = float(input("Insert a number: "))

if num > 0:
    print("Positive number.")
elif num < 0:
    print("Negative number.")
else:
    print("That's a zero.")


# Even or odd numbers.

number = float(input("Insert a number: "))

if number % 2 == 0:
    print("Even number.")
else:
    print("Odd number.")
