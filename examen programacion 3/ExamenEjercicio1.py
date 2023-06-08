# Programacion 3 N-613
# Jesus Apolinar V-30740060
# Juan Barreto V-31106376
# Isabel Diaz V-30605281

# Escribir un programa que calcule el factorial de un numero ingresado por el usuario
# usando el bucle while

#Se ingresa el numero para calcular su factorial
n = int(input("Ingrese un numero para calcular su factorial: "))
i=1

#Se inicializa el factorial en n*1
factorial = 1

#Bucle while para iterar la operacion de un factorial
while(i<n):
    factorial += factorial*i
    i=i+1

#Salida de datos
print("el factorial de ",n," es: ",factorial)