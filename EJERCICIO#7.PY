#Desarrolle un algoritmo que lea de un registro: el nombre, la edad, el sexo, el estado civil de cualquier persona e imprima el nombre de la persona, si corresponde a un hombre casado mayor de 40 años o a una mujer soltera menor de 50 años. 
nombre = input("ingrese el nombre")
edad = int(input("ingrese la edad"))
sexo = input("ingrese el sexo(masculino,fememino):")
estado_civil = input("ingrese el estado civil(soltero,casado):")

if (sexo == "masculino" and estado_civil == "casado" and edad > 40)or(sexo == "femenino" and estado_civil == "soltero" and edad < 50):
   
    print(f"nombre : [nombre]","si corresponde" )
    
else:
   
    print("no cumple con los criterios")
    