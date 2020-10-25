# Celsius to Fehrenheit.

cel = int(input("Insert a number in celsius: "))

cel = round(cel * (9/5) + 32)
print(str(cel) + " F.")

# Fehrenheit to Celsius.

feh = int(input("Insert a number in fehrenheit: "))

feh = round((feh - 32)*( 5 / 9 ))
print(str(feh) + " C.")