peso = int(input("ingresa tu peso en (kg): "))
altura = float(input("ingresa tu altura en (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"tu imc es {imc:.2f}. Bajo peso.")
elif 18.5 <= imc < 25:
    print(f"tu imc es {imc:.2f}. normal.")
else:
    print(f"tu imc es {imc:.2f}. obesidad.")
