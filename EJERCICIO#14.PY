# Desarrollar un algoritmo que evalué la siguiente expresión aritmética 1/n.
def evaluar_expresion(n):
    # Verificamos si n es cero
    if n == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        # Calculamos y mostramos el resultado de la expresión 1/n
        resultado = 1 / n
        print(f"El resultado de 1/{n} es: {resultado:.4f}")  # Se muestra con 4 decimales para mayor claridad

# Solicitar el valor de n al usuario
try:
    n = float(input("Introduce el valor de n: "))
    evaluar_expresion(n)
except ValueError:
    print("Error: Por favor ingresa un número válido.")
