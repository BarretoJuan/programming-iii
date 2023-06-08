# Programacion 3 N-613
# Jesus Apolinar V-30740060
# Juan Barreto V-31106376
# Isabel Diaz V-30605281

# Escribir un programa que solicite al usuario una lista de numeros y luego calcule la media de los numeros, utilizando
# una estructura de control

#Se indica la cantidad de numeros a añadir a la lista
nNum = int(input("Ingrese la cantidad de numeros a ingresar para calcular su media: "))

#inicializacion de variables
i=1
listaNum = []

#Se itera el ciclo while para ingresar la cantidad de numeros indicados
while(i<=nNum):

    nInput = int(input("Ingrese un numero (Numero: "+str(i)+"/"+str(nNum)+"): "))

    #método append para ingresar elementos a la lista
    listaNum.append(nInput)
    i=i+1

#inicializacion de variables para generar la suma de los elementos de la lista
n=0
suma=0

#bucle while para suumar los elementos de la lista
while (n<nNum):
    suma=suma+listaNum[n]
    n=n+1

#promedio = a la suma de los elementos de la lista entre el numero de elementos de la lista
promedio = suma / nNum
StrListNum = str(listaNum)

#salida de datos
print("El promedio de los numeros: "+StrListNum+" es: "+str(promedio))