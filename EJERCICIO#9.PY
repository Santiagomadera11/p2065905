#Dados tres números enteros únicos, a, b y c. Elabore un algoritmo que los ordene de mayor a menor e imprímalos.
numA = int(input("ingrese el primer numero"))
numB = int(input("ingrese el segundo numero"))
numC = int(input("ingrese el tercer numero"))

numeros = [numA,numB,numC]
numeros.sort(reverse = True)
print("numeros ordenados de mayor a menor:", numeros)
