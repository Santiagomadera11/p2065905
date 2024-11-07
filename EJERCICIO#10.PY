#Haga un algoritmo que permita a un estudiante efectuar el cálculo correspondiente a su nota final. 
nota1 = float(input("ingrese la primera calificasion"))
nota2 = float(input("ingrese la segunda calificasion"))
nota3 = float(input("ingrese la tercera calificasion"))

notas = [nota1,nota2,nota3]
notas.sort(reverse=True)

nota_final = (notas[0] + notas[1])/2
print(f"la calificasion final es :{nota_final:.2f}")
