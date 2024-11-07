#Prepare un algoritmo que identifique e imprima el número medio de un conjunto de tres números únicos. El número medio es aquel que no es el menor ni el mayor. 
a = float(input("ingrese el primer numero"))
b = float(input("ingrese el segundo numero"))
c = float(input("ingrese el tercer numero"))

if ( a > b and a < c ) or ( a < b and a > c ):
    print("en numero medio es ",a)

elif ( b > a and b > c ) or ( b < a and b > c ):
    print("el numero medio es ", b)
else:
    ( c > a and c > b ) or ( c < a and c > b )
    print("numero medio es ", c)
    
    print(f"el numero medio es:")
    