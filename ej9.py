num = int(input ("Ingrese un numero: "))

divisibles = []
if num % 4 == 0:
    divisibles.append(4)
if num % 6 == 0:
    divisibles.append(6)
if num % 8 == 0:
    divisibles.append(8)
if num % 10 == 0:
    divisibles.append(10)

if divisibles:
    print(f"El número es divisible por: {', '.join(map(str, divisibles))}.")
else:
    print("El número no es divisible por 4, 6, 8 o 10.")