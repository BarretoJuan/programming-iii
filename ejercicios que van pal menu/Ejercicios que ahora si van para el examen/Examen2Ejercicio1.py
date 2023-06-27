# #Juan Barreto V31106376
# Programacion III N613
# Segundo examen primer corte

# desarrollar un programa que genere tablas de multiplicar para un rango de numeros especificado por el usuario
# utilizar el ciclo for

#inicio del programa
print("Bienvenido, en el siguiente programa se desarrollarán tablas de multiplicar para un rango determinado")

#Entrada de limites para generar las tablas
limInf = int(input("Ingrese el límite inferior para generar las tablas de multiplicar: "))
limSup = int(input("ingrese el limite superior para generar las tablas de multiplicar: "))

#si el limite inferior ingresado es mayor al limite superior, no se continúa el programa
start = True
if(limInf > limSup):
    print("El limite inferior proporcionado es mayor al limite superior")
    start = False

# si se cumple las condiciones del limite, se procede
if(start == True):

    #for anidado para recorrer cada numero de los limites y generar la tabla de multiplicar del 1 al 10 cada numero
    for i in range(limInf,limSup+1):
        print(" ")
        print("***TABLA DEL ",i,"***")
        for n in range(1,11):
            print(i, "x", n, " = ", i*n)

#Este input tiene como funcion evitar que el programa se cierre luego de mostrar la salida de datos, en caso de ejecutarlo en la linea de comandos
noPares = input("Presione cualquier tecla para finalizar el programa ")


