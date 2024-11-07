#.Escriba un algoritmo que acepte o rechace una pieza en forma de varilla

def aceptar_o_rechazar_pieza(longitud, diametro):
    # Definimos la densidad
    densidad = 3.5  # en gr/cm³
    
    # Verificamos las condiciones de longitud
    if not (7.5 < longitud <= 9):
        print("Pieza rechazada: Longitud fuera de rango.")
        return
    
    # Verificamos las condiciones de diámetro
    if not (0.5 <= diametro <= 1.3):
        print("Pieza rechazada: Diámetro fuera de rango.")
        return
    
    # Calculamos la masa
    masa = (diametro * longitud) / densidad
    
    # Verificamos las condiciones de masa
    if masa > 5.8:
        print("Pieza rechazada: Masa excede el límite permitido.")
        return
    
    # Si todas las condiciones se cumplen
    print("Pieza aceptada.")





    