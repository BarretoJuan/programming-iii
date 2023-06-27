# Lunes 19 de junio de 2023
# Juan Barreto V31106376

import random

# #Se tiene un programa que pida al usuario generar n cantidad de numeros pseudoaleatorios
# a continuacion, se realizarán las operaciones de suma, resta, multiplicación y division a todos los 
# elementos generados.


print("En el siguiente programa se generarán dos números aleatorios, luego")
print("se sumarán, restarán, multiplicarán y se dividirán a los números generados")
print("")
n = 2
listNum = []

#Se generan los numeros aleatorios
for i in range (0,n):
    m = random.randint(1, 200)
    listNum.append(m)

#se inicializan las variables de suma, resta, multiplicacion y division
suma =0
resta =0
multiplicacion = 1
division = 1

#Se imprimen los numeros generados
print("Los numeros generados fueron: ")
for i in range (0,n):
    print(listNum[i])

#Se generan las operaciones
suma = listNum[0]+listNum[1]
resta = listNum[0]-listNum[1]
multiplicacion = listNum[0]*listNum[1]
division = listNum[0]/listNum[1]


#Se muestran los resultados
print("La suma de los numeros generados es: ",suma)
print("La resta de los numeros generados es: ",resta)
print("La multiplicación de los numeros generados es: ",multiplicacion )
print("La division de los numeros generados es: ",division)   
