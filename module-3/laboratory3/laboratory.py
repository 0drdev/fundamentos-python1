year = int(input("Introduce un año:"))

if year >= 1582:
    if (year % 4 == 0 and year != 0) or (year % 400 == 0):
        print("Año Bisiesto")
    else:
        print("Año normal")
else:
    print("No dentro del período del calendario Gregoriano")
