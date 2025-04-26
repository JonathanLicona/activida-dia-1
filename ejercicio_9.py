anio = int(input("introduce un año"))
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("f el año {anio} es bisiesto")
else:
    print(f"el año{anio} no es binario")
