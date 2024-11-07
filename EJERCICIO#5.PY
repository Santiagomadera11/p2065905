#desarrollar un programa que capture tres números e imprima por pantalla cual es el número mayor, el menor, cuales son iguales, si los tres diferentes. 
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

mayor = max(num1,num2,num3)
menor = min(num1,num2,num3)

print ("numero mayor es: ", mayor)
print ("numero menor es: ", menor)

if num1 > num2 and num1 > num3:
    if num2 > num1 and num2 > num3:
       if num3 > num1 and num3 > num2:   
         print("numero mayor es:",num1,num2,num3)


if num1 < num2 and num1 < num3:
    if num2 < num1 and num2 < num3:
       if num3 < num1 and num3 < num2:   
         print("numero menor es:",num1,num2,num3)


if num1 == num2 == num3:
     print("Los tres números son iguales.")

elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Hay al menos dos números iguales.")

else:
    print("Los tres números son diferentes.")