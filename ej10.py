num = int(input ("Ingrese un numero: "))

print(f"Múltiplos de 3 menores que {num}:")
for i in range(3, num, 3):
    print(i)
