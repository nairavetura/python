num = int(input ("Ingrese un numero: "))

suma_divisor = sum(i for i in range(1, num) if num % i == 0)

if suma_divisor == num:
    print(f"{num} es un número perfecto.")
else:
    print(f"{num} no es un número perfecto.")
