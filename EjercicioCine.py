# # JUAN BARRETO 31106376 
# PROGRAMACION 3 N-613 
# Elabore un programa que simula la ventas de boletos de un empresa de entretenimiento (CINE), donde el valor de los boleto dependera de la clasificacion de la pelicula

# # A = 2$

# B = 3$

# C = 3.5$

# D y E = 5$

# se aplicara descuento los dias lunes, jueves y viernes del 20%

# Se aplicara descuento por niño y 3era edad de 50%

#informacion inicial
print("Bienvenido al sistema de ventas de boletos del cine XY")
print("El precio del boleto dependerá de la clasificación de la película")
print("Adicionalmente, se aplicará un descuento del 20% los dias Lunes, Jueves y Viernes, y ")
print("un descuento del 50% a niños y adultos mayores")
print("Precio del boleto por categoría: ")
print("Categoria A) 2$")
print("Categoria B) 3$")
print("Categoria C) 3.5$")
print("Categoria D) 5$")
print("Categoria E) 5$")

#se pregunta al usuario la categoria de la pelicula
clasificacion = str(input("Ingrese la categoría de la película: "))

#se evalua si la categoria ingresada por el usuario corresponde con alguna de las categorias de la pelicula
if (clasificacion == "A"):
    start = True
    precioBoleto = 2
elif (clasificacion == "B"):
    start = True
    precioBoleto = 3
elif (clasificacion == "C"):
    start = True
    precioBoleto = 3.5
elif (clasificacion == "D" or clasificacion == "E"):
    start = True
    precioBoleto = 5    
else:
    print("Clasificacion no valida")
    start = False

#si la categoria fue valida, se inicia el ingreso de datos para la factura
if (start == True):
    
    #cantidad de boletos y dia de la semana
    nBoletoRegular = int(input("Ingrese la cantidad de boletos regulares: "))
    nBoletoDescuento = int(input("Ingrese la cantidad de boletos para niños o adultos mayores (50% de descuento): "))
    descuentoBoleto = 50
    diaSemana = str(input("Ingrese el día de la semana (Lunes, Jueves y Viernes tienen un descuento del 20%): "))

    #se evalua si el dia de la semana calculado es aplicable para descuento
    if (diaSemana == "Lunes" or diaSemana == "Jueves" or diaSemana == "Viernes"):
        print("el día seleccionado (", diaSemana, ") le otorga un 20% de descuento a todos sus boletos")
        descuentoDia = 20
    else:
        print("el día seleccionado (", diaSemana, ") no es aplicable para descuentos")
        descuentoDia = 0
    
    #se calculan los montos a pagar
    montoBoletosRegulares= nBoletoRegular*precioBoleto
    montoBoletosDescuento = nBoletoDescuento*precioBoleto - ((nBoletoDescuento*precioBoleto)*descuentoBoleto/100)

    totalSinDescuentoDia = montoBoletosDescuento+montoBoletosRegulares
    totalConDescuentoDia = (totalSinDescuentoDia) - (totalSinDescuentoDia*descuentoDia/100)

    #print final de la factura
    print(" ")
    print("**FACTURA**")
    print("Día de la semana: ",diaSemana)
    print("Descuento del día: ",descuentoDia,"%")
    print("Categoría de la pelicula: ",clasificacion)
    print("Precio base del boleto: ",precioBoleto,"$")
    print(" ")
    print("Número de boletos regulares: ",nBoletoRegular)
    print("Monto a pagar por los boletos regulares: ",montoBoletosRegulares,"$")
    print("Número de boletos para niños o adultos mayores (50% de descuento): ",nBoletoDescuento)
    print("Monto a pagar por los boletos de niños o adultos mayores: ",montoBoletosDescuento,"$")
    print("**TOTAL**")
    print("Monto a pagar sin descuento del día: ", totalSinDescuentoDia,"$")
    print("Monto a pagar con el descuento del día: ",totalConDescuentoDia,"$")
    print("Muchas gracias, que tenga un buen día!")

