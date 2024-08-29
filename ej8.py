num = int(input ("Ingrese un numero: "))

if num % 4 == 0 or num % 6 == 0 or num % 8 == 0 or num % 10 == 0:
    print("El número es divisible por 4, 6, 8 o 10.")
else:
    print("El número no es divisible por 4, 6, 8 o 10.")