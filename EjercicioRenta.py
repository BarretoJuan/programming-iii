  #  JUAN BARRETO 31106376 N613
# # Escribir un programa que pregunte al usuario su renta anual
# y muestre por pantalla el tipo impositivo que le corresponde

# Menos de 10000$, 5%
# Entre 10000$ y 20000$, 14%
# Entre 20000$ y 35000$, 20%
# Entre 35000$ y 60000$, 30%
# Más de 60000$ 45%

#Inicio
print("En el siguiente programa se le preguntará su renta, para informarle el porcentaje de su tipo impositivo correspondiente")
print("")
print("**Tabla de valores**")
print(" Menos de 10000$, 5%")
print("Entre 10000$ y 20000$, 15%")
print("Entre 20000$ y 35000$, 20%")
print("Entre 35000$ y 60000$, 30%")
print("Más de 60000$, 45%")

#entrada de datos
n = int(input("Ingrese su renta: "))

if(n<10000):
    print("Su valor impositivo correspondiente es del 5%")
    impuesto = 0.05*n
    print("Su valor impositivo es de ",str(impuesto))
elif(n>=10000 and n<20000):
    print("Su valor impositivo correspondiente es del 15%")
    impuesto = 0.15*n
    print("Su valor impositivo es de ",str(impuesto))
elif(n>=20000 and n<35000):
    print("Su valor impositivo correspondiente es del 20%")
    impuesto = 0.20*n
    print("Su valor impositivo es de ",str(impuesto))
elif(n>=35000 and n<60000):
    print("Su valor impositivo correspondiente es del 30%")
    impuesto = 0.30*n
    print("Su valor impositivo es de ",str(impuesto))
else:
    print("Su valor impositivo correspondiente es del 45%")   
    impuesto = 0.45*n
    print("Su valor impositivo es de ",str(impuesto))

dontStopUnexpectedly = input("") 