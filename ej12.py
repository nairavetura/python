nota = float(input ("Ingrese la calificacion: "))

if 0 <= nota <= 2:
    evaluacion = "Muy Malo"
elif 3 <= nota <= 4:
    evaluacion = "Malo"
elif 5 <= nota <= 6:
    evaluacion = "Regular"
elif 7 <= nota <= 8:
    evaluacion = "Muy Bueno"
elif 9 <= nota <= 10:
    evaluacion = "Excelente"
else:
    evaluacion = "Calificación fuera de rango"

print(f"La evaluación es: {evaluacion}")
