total_cuenta = float(input("cual fue el monto a pagar de su cuenta :$"))

print("¿cuanto porcentaje quieres dejar de  propina?")
print("1. 10%")
print("2. 15%")
print("3. 20%")
porcentaje = int(input("selecciona 1,2 o 3:"))

if porcentaje == 1:
    propina = total_cuenta * 0.10
elif porcentaje == 2:
    propina = total_cuenta * 0.15
elif porcentaje == 3:
    propina = total_cuenta * 0.20
else:
    print("esta opcion no es valida")
    propina = 0

print(f"la propina es: ${propina:.2f}")
