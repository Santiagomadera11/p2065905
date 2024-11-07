#desarrollar el algoritmo dado como dato el sueldo de un trabajador, le aplica un aumento del 15% si su sueldo es inferior a $300.000. 
sueldo_IN = float(input("Ingrese el sueldo inicial del trabajador:"))

  
if sueldo_IN < 300000:
    AU = sueldo_IN * 0.15
    nuevo_SLD = sueldo_IN + AU
else:
    nuevo_SLD = sueldo_IN

print("El nuevo sueldo del trabajador es:", nuevo_SLD)