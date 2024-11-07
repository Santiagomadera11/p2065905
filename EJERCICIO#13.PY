#desarrollar un algoritmo que halle la nota total de una materia en el SENA, y determine si la gano o la reprobó 
def calcular_nota_total(examen_teorico, practica_proyecto, participacion):
    # Ponderaciones
    peso_examen_teorico = 0.40
    peso_practica_proyecto = 0.40
    peso_participacion = 0.20
    
    # Calcular la nota total ponderada
    nota_total = (examen_teorico * peso_examen_teorico) + (practica_proyecto * peso_practica_proyecto) + (participacion * peso_participacion)
    
    return nota_total

def determinar_estado(nota_total):
    # Determinar si el estudiante aprobó o reprobó
    if nota_total >= 3.0:
        return "Aprobado"
    else:
        return "Reprobado"

# Solicitar al usuario las notas
examen_teorico = float(input("Introduce la nota del examen teórico (1.0 - 5.0): "))
practica_proyecto = float(input("Introduce la nota de prácticas o proyectos (1.0 - 5.0): "))
participacion = float(input("Introduce la nota de participación o asistencia (1.0 - 5.0): "))

# Calcular la nota total
nota_total = calcular_nota_total(examen_teorico, practica_proyecto, participacion)

# Mostrar la nota total
print(f"\nLa nota total es: {nota_total:.2f}")

# Determinar si aprobó o reprobó
estado = determinar_estado(nota_total)

# Mostrar el resultado final
print(f"Estado final: {estado}")
