#Desarrolle un algoritmo que lea un número, en caso de ser negativo lo imprima junto con su positivo. 
num= int(input("Ingrese un número: "))

if num < 0:
    print("El número es negativo:", num)
    print("Su positivo es:", -num)
