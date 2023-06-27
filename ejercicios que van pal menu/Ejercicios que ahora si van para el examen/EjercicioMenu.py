def Menu():
    tryAgain = True
    while tryAgain == True:
        print("En el siguiente menú podrá ejecutar los ejercicios entregados durante el primer corte de programación III N-613, realizados por Juan Barreto V31106376")
        print("1) Ejercicio NumPrimo")
        print("2) Ejercicio Panaderia sin paises")
        print("3) Ejercicio Panaderia con paises")
        print("4) Ejercicio Cine")
        print("5) Ejercicio Renta")
        print("6) Ejercicio Pizza")
        print("7) Ejercicio Examen2")
        answer = int(input("Ingrese su respuesta: "))
        if(answer==1):
            EjercicioNumPrimo()
            tryAgain=False
        elif(answer==2):
            EjercicioPanaderia1()
            tryAgain=False
        elif(answer==3):
            EjercicioPanaderia2()
            tryAgain=False
        elif(answer==4):
            EjercicioCine()
            tryAgain=False
        elif(answer==5):
            EjercicioRenta()
            tryAgain=False
        elif(answer==6):
            EjercicioPizza()
            tryAgain=False
        elif(answer==7):
            EjercicioExamen2()
            tryAgain=False    
        else:
            print("Usted ingresó un valor no válido para el menú, intente de nuevo")
            tryAgain = True

def EjercicioNumPrimo():
    i = input("Ingresa un numero para determinar si es un numero primo")
        #Se verifica si el numero ingresado es 0 o 1
    if(i == 0 or i ==1 ):
        print(i," no es primo")
    #Se verifica si el numero ingresado es alguno de los 4 menores numeros primos
    elif(i==2 or i==3 or i==5 or i==7):
        print(i," es primo")
    #De ser divisible entre alguno de los cuatro menores numeros primos, se considera no primo
    elif(i%2==0 or i%3==0 or i%5==0 or i%7==0):
        print(i," no es primo")
    #De lo contrario, es primo
    else:
        print(i," es primo")


def EjercicioPanaderia1():
        #en una panaderia se elaboran 4000 panes diarios, de los cuales 1000 
    #son panes franceses, otros 1000 son panes dulces, 500 son 
    # panes de perros calientes, otros 500 son panes de hamburguesa
    # 700 son panes de sandwich y 300 panes de queso
    # realizar un sistema de ventas donde se incluya el iva y el total
    # solamente usando la condicion if

    #Inventario disponible
    print("**DISPONIBILIDAD ACTUAL DE INVENTARIO**")
    print("Pan Frances: 1000 unidades")
    print("Pan Dulce: 1000 unidades")
    print("Pan de Perro Caliente: 500 unidades")
    print("Pan de Hamburguesa: 500 unidades")
    print("Pan de Sanwich: 700 unidades")
    print("Pan de Queso: 300 unidades")
    print(" ")

    #Se pregunta al usuario el precio de cada articulo
    precioPFrances = int(input("Ingrese el precio del pan frances: "))
    precioPDulce = int(input("Ingrese el precio del pan dulce: "))
    precioPPerroCaliente =  int(input("Ingrese el precio del pan de perro caliente: "))
    precioPHamburguesa = int(input("Ingrese el precio del pan de hamburguesa: "))
    precioPSandwich = int(input("Ingrese el precio del pan de sandwich: "))
    precioPQueso = int(input("Ingrese el precio del pan de queso: "))


    #se pregunta al usuario la cantidad de cada articulo y se verifica si esa cantidad está disponible en el inventario
    input1 = int(input("Ingrese la cantidad de pan frances (1000 unidades restantes): "))
    if(input1 <= 1000):
        cantPFrances = input1
    else: 
        print("No hay stock de este articulo")
        cantPFrances=0

    input2 = int(input("Ingrese la cantidad de pan dulce (1000 unidades restantes): "))
    if(input2 <= 1000):
        cantPDulce = input2
    else:
        print("No hay stock de este articulo")
        cantPDulce=0

    input3 = int(input("Ingrese la cantidad de pan de perro caliente (500 unidades restantes): "))
    if(input3 <= 500):
        cantPPerroCaliente = input3
    else:
        print("No hay stock de este articulo")
        cantPPerroCaliente=0

    input4 = int(input("Ingrese la cantidad de pan de hamburguesa (500 unidades restantes): "))
    if(input4 <= 500):
        cantPHamburguesa = input4
    else:
        print("No hay stock de este articulo")
        cantPHamburguesa=0

    input5 = int(input("Ingrese la cantidad de pan de sandwich (700 unidades restantes): "))
    if(input5 <= 700):
        cantPSandwich = input5
    else:
        print("No hay stock de este articulo")
        cantPSandwich=0

    input6 = int(input("Ingrese la cantidad de pan de queso (300 unidades restantes): "))
    if(input6 <= 300):
        cantPQueso = input6
    else:
        print("No hay stock de este articulo")
        cantPQueso=0

    #se establecen los montos de cada articulo y el monto total con y sin iva
    montoPFrances = precioPFrances*cantPFrances
    montoPDulce = precioPDulce*cantPDulce
    montoPPerroCaliente = precioPPerroCaliente*cantPPerroCaliente
    montoPHamburguesa = precioPHamburguesa*cantPHamburguesa
    montoPSandwich = precioPSandwich*cantPSandwich
    montoPQueso = precioPQueso*cantPQueso
    precioSinIVA= montoPFrances + montoPDulce + montoPPerroCaliente + montoPHamburguesa + montoPSandwich + montoPQueso
    cantIVA = precioSinIVA*0.16
    precioConIVA=precioSinIVA+cantIVA

    #se calcula el inventario restante de cada articulo
    resPFrances=1000-cantPFrances
    resPDulce=1000-cantPDulce
    resPPerroCaliente=500-cantPPerroCaliente
    resPHamburguesa=500-cantPHamburguesa
    resPSandwich=700-cantPSandwich
    resPQueso=300-cantPQueso

    #salida final de datos
    print("***MONTO A PAGAR:***")
    print("Monto: ",precioSinIVA)
    print("IVA (16.00%): ",cantIVA)
    print("Monto con IVA: ",precioConIVA)
    print("")
    print("**Inventario Restante**")
    print("Pan Frances: ",resPFrances," unidades")
    print("Pan Dulce: ",resPDulce," unidades")
    print("Pan de Perro Caliente: ",resPPerroCaliente," unidades")
    print("Pan de Hamburguesa: ",resPHamburguesa," unidades")
    print("Pan de Sanwich: ",resPSandwich," unidades")
    print("Pan de Queso: ",resPQueso," unidades")

def EjercicioPanaderia2():
    # # JUAN BARRETO 31106376 
    # PROGRAMACION 3 N-613 
    #en una panaderia se elaboran 4000 panes diarios, de los cuales 1000 
    #son panes franceses, otros 1000 son panes dulces, 500 son 
    # panes de perros calientes, otros 500 son panes de hamburguesa
    # 700 son panes de sandwich y 300 panes de queso
    # realizar un sistema de ventas donde se incluya el iva y el total
    # solamente usando la condicion if

    # Para este programa se iniciará mostrando el inventario actual, se pedirá al usuario ingresar 
    # el precio de cada articulo y la cantidad de ventas de cada articulo a registrar
    # se verificará si la cantidad a registrar sobrepasa al stock actual.
    # Finalmente se mostrará el precio sin IVA, el monto del IVA y el precio con IVA, junto con un  resumen del 
    # inventario restante

    # además, el programa preguntará al usuario ingresar el descuento a aplicar a cada región de America, tomando
    # en cuenta las regiones de Norteamérica, Centroamérica, Sudamérica, y el Caribe, si el pais ingresado por el usuario
    # no puede ser identificado entre alguno de los paises de América, Se asumirá un descuento del 0%

    #diccionario de paises con sus regiones
    paises = {
                        "Antigua y Barbuda":"Caribe",
                        "Argentina": "Sudamérica",
                        "Bahamas":"Caribe",
                        "Barbados":"Caribe",
                        "Belice":"Centroamérica",
                        "Bolivia":"Sudamérica",
                        "Brasil":"Sudamérica",
                        "Canada":"Norteamérica",
                        "Chile":"Sudamérica",
                        "Colombia":"Sudamérica",
                        "Costa Rica":"Centroamérica",
                        "Cuba":"Caribe",
                        "Dominica":"Caribe",
                        "República Dominicana":"Caribe",
                        "Ecuador":"Sudamérica",
                        "El Salvador":"Centroaméricar",
                        "Granada":"Caribe",
                        "Guatemala":"Centroamérica",
                        "Guyana":"Sudamérica",
                        "Haití":"Caribe",
                        "Honduras":"Centroamérica",
                        "Jamaica":"Caribe",
                        "México":"Norteamérica",
                        "Nicaragua":"Centroamérica",
                        "Panamá":"Centroamérica",
                        "Paraguay":"Sudamérica",
                        "Perú":"Sudamérica",
                        "San Cristóbal y Nieves":"Caribe",
                        "Santa Lucía":"Caribe",
                        "San Vicente y Granadinas":"Caribe",
                        "Suriname":"Sudamérica",
                        "Trinidad y Tobago":"Caribe",
                        "Estados Unidos":"Norteamérica",
                        "Uruguay":"Sudamérica",
                        "Venezuela":"Sudamérica",
                        }

    #Inventario disponible
    print("**DISPONIBILIDAD ACTUAL DE INVENTARIO**")
    print("Pan Frances: 1000 unidades")
    print("Pan Dulce: 1000 unidades")
    print("Pan de Perro Caliente: 500 unidades")
    print("Pan de Hamburguesa: 500 unidades")
    print("Pan de Sandwich: 700 unidades")
    print("Pan de Queso: 300 unidades")
    print(" ")
    print("Esta panadería maneja un descuento para las diferentes regiones de América")
    print("Si el país ingresado no pertenece a América, no tendrá descuento")
    print(" ")


    #Se pregunta al usuario el precio de cada articulo y el descuento a aplicar a cada región de América
    print("***ESTABLECIMIENTO DE PRECIOS Y DESCUENTOS***")
    precioPFrances = int(input("Ingrese el precio del pan frances: "))
    precioPDulce = int(input("Ingrese el precio del pan dulce: "))
    precioPPerroCaliente =  int(input("Ingrese el precio del pan de perro caliente: "))
    precioPHamburguesa = int(input("Ingrese el precio del pan de hamburguesa: "))
    precioPSandwich = int(input("Ingrese el precio del pan de sandwich: "))
    precioPQueso = int(input("Ingrese el precio del pan de queso: "))
    print(" ")
    descuentoNorte = int(input("Ingrese el descuento a aplicar a los paises de Norteamérica: "))
    descuentoCentro = int(input("Ingrese el descuento a aplicar a los países de Centroamérica: "))
    descuentoSur = int(input("Ingrese el descuento a aplicar a los países de Sudamérica: "))
    descuentoCaribe = int(input("Ingrese el descuento a aplicar a los países del Caribe: "))
    print(" ")
    IVA = int(input("Ingrese el porcentaje del IVA a aplicar (Impuesto al valor agregado): "))


    #se pregunta al usuario la cantidad de cada articulo y se verifica si esa cantidad está disponible en el inventario
    print(" ")
    print("***INGRESO DE CANTIDADES PARA LA COMPRA***")
    input1 = int(input("Ingrese la cantidad de pan frances (1000 unidades restantes) (precio: "+ str(precioPFrances)+" $): "))
    if(input1 <= 1000):
        cantPFrances = input1
    else: 
        print("No hay stock de este articulo")
        cantPFrances=0

    input2 = int(input("Ingrese la cantidad de pan dulce (1000 unidades restantes) (precio: "+ str(precioPDulce)+" $): "))
    if(input2 <= 1000):
        cantPDulce = input2
    else:
        print("No hay stock de este articulo")
        cantPDulce=0

    input3 = int(input("Ingrese la cantidad de pan de perro caliente (500 unidades restantes) (precio: "+ str(precioPPerroCaliente)+" $): "))
    if(input3 <= 500):  
        cantPPerroCaliente = input3
    else:
        print("No hay stock de este articulo")
        cantPPerroCaliente=0

    input4 = int(input("Ingrese la cantidad de pan de hamburguesa (500 unidades restantes) (precio: "+ str(precioPHamburguesa)+" $): "))
    if(input4 <= 500):
        cantPHamburguesa = input4
    else:
        print("No hay stock de este articulo")
        cantPHamburguesa=0

    input5 = int(input("Ingrese la cantidad de pan de sandwich (700 unidades restantes) (precio: "+ str(precioPSandwich)+" $): "))
    if(input5 <= 700):
        cantPSandwich = input5
    else:
        print("No hay stock de este articulo")
        cantPSandwich=0

    input6 = int(input("Ingrese la cantidad de pan de queso (300 unidades restantes) (precio: "+ str(precioPQueso)+" $): "))
    if(input6 <= 300):
        cantPQueso = input6
    else:
        print("No hay stock de este articulo")
        cantPQueso=0

    #Se pregunta al usuario su país de origen
    print(" ")
    print("***PAIS DE ORIGEN***")
    paisInput = str(input("Ingrese su país de origen: "))
    print(" ")
    paisExiste=0

    #Se verifica si el pais ingresado existe en el diccionario de paises de america
    for i in paises:
        if (paisInput == i):
            paisExiste=paisExiste+1
        
    #si el pais existe, se asigna el monto del descuento a la region del pais ingresado
    if(paisExiste==1):
        if(paises[paisInput]== "Norteamérica"):
            descuento = descuentoNorte
        elif(paises[paisInput]=="Centroamérica"):
            descuento = descuentoCentro
        elif(paises[paisInput]=="Sudamérica"):
            descuento = descuentoSur
        elif(paises[paisInput]=="Caribe"):
            descuento = descuentoCaribe    
        print("El pais ",paisInput," Sí existe en America y su región es: ",
            paises[paisInput], " y su compra contará con el ",descuento,"% de descuento")
        region = paises[paisInput]
    else:
        print("El pais ",paisInput," No existe en America, por lo tanto, su compra no contará con descuento")
        descuento = 0
        region = "Desconocido"

    #se establecen los montos de cada articulo y el monto total sin descuento, con descuento, y finalmente se le añade el IVA
    montoPFrances = precioPFrances*cantPFrances
    montoPDulce = precioPDulce*cantPDulce
    montoPPerroCaliente = precioPPerroCaliente*cantPPerroCaliente
    montoPHamburguesa = precioPHamburguesa*cantPHamburguesa
    montoPSandwich = precioPSandwich*cantPSandwich
    montoPQueso = precioPQueso*cantPQueso
    precioSinDescuento= (montoPFrances + montoPDulce + montoPPerroCaliente
                + montoPHamburguesa + montoPSandwich + montoPQueso)
    precioConDescuento=precioSinDescuento - (precioSinDescuento*descuento)/100
    cantIVA = (precioConDescuento*IVA)/100
    precioConIVA=precioConDescuento+cantIVA

    #se calcula el inventario restante de cada articulo
    resPFrances=1000-cantPFrances
    resPDulce=1000-cantPDulce
    resPPerroCaliente=500-cantPPerroCaliente
    resPHamburguesa=500-cantPHamburguesa
    resPSandwich=700-cantPSandwich
    resPQueso=300-cantPQueso

    #salida final de datos
    print("***MONTO A PAGAR:***")
    print("Monto: ",precioSinDescuento, "$")
    print("Pais: ",paisInput)
    print("Region", region)
    print("Descuento Regional", descuento,"%")
    print("Monto con descuento: ",precioConDescuento,"$")
    print("Monto IVA (",IVA,"%): ",cantIVA,"$")
    print("Total a pagar: ",precioConIVA,"$")
    print("")
    print("**Inventario Restante**")
    print("Pan Frances: ",resPFrances," unidades")
    print("Pan Dulce: ",resPDulce," unidades")
    print("Pan de Perro Caliente: ",resPPerroCaliente," unidades")
    print("Pan de Hamburguesa: ",resPHamburguesa," unidades")
    print("Pan de Sanwich: ",resPSandwich," unidades")
    print("Pan de Queso: ",resPQueso," unidades")    

def EjercicioCine():
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



def EjercicioRenta():
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
def EjercicioPizza():
        

    # La pizzeria bella napoli ofrece pizzas vegetarianas y no
    # vegetarianas a sus clientes. Los ingredientes para cada
    # tipo de pizza aparecen a continuación:

    # Ingredientes vegetarianos: pimiento y tofu
    # Ingredientes no vegetarianos: peperoni, jamon y salmon.

    # Escribir un programa que pregunte al usuario si quiere 
    # una pizza vegetariana o no, y en funcion de la respuesta
    # le muestre un menú con los ingredientes disponibles para
    # que elija. Solo se puede elegir un ingrediente además de
    # la mozzarella, y el tomate que están en todas las pizzas.
    # Al final se debe mostrar por pantalla si la pizza elegida es
    # vegetariana o no y todos los ingredientes que lleva

    #declaracion de tuplas
    ingredientesVegetarianos = ("Pimiento", "Tofu")
    ingredientesNoVegetarianos = ("Peperoni", "Jamón", "Salmón")


    #inicio
    print("Bienvenido/a a la Pizzeria Bella Napoli, contamos con menú vegetariano y no vegetariano")
    print("Todas nuestras pizzas incluyen mozzarella y tomate")

    #loop while para determinar el tipo de pizza
    loop=True
    while loop==True:

        tipoPizzaEntrada = input("Desea una pizza vegetariana? 1)Si 2)No:")

        if(tipoPizzaEntrada == "1"):
            isVegetariana = True
            loop = False
            print("Perfecto! se le mostrará un menú vegetariano")

        elif(tipoPizzaEntrada == "2"):
            isVegetariana = False
            loop = False
            print("Perfecto! se le mostrará un menú no vegetariano")

        else:
            print("Respuesta no válida, intente de nuevo")

    print("Ingrese el ingrediente a elegir de su pizza: ")

    #escoger pizza vegetariana
    if(isVegetariana):
        print("**Ingredientes**")
        i = 0
        for i in ingredientesVegetarianos:
            print(i)
        print("**********")
        

        loop2 = True
        while loop2==True:
            ingrediente = input("Seleccione su ingrediente de la lista: ")
            ingredienteExiste=False
            for i in ingredientesVegetarianos:  
                if(ingrediente == i):
                    ingredienteExiste =True
                    loop2=False
            if(ingredienteExiste ==False):
                print("Usted ingresó un ingrediente invalido, intente de nuevo")
            
        print("Usted seleccionó una pizza vegetariana de ingrediente: ",ingrediente, ", Tomate, y Mozarella")

    #escoger pizza no vegetariana
    elif(isVegetariana==False):
        print("**Ingredientes**")
        i = 0
        for i in ingredientesNoVegetarianos:
            print(i)
        print("**********")
        

        loop2 = True
        while loop2==True:
            ingrediente = input("Seleccione su ingrediente de la lista: ")
            ingredienteExiste=False
            for i in ingredientesNoVegetarianos:  
                if(ingrediente == i):
                    ingredienteExiste =True
                    loop2=False
            if(ingredienteExiste ==False):
                print("Usted ingresó un ingrediente invalido, intente de nuevo")
            
        print("Usted seleccionó una pizza NO vegetariana de ingredientes: ",ingrediente, ", Tomate, y Mozarella")

    doNotEndUnexpectedly = input("")

        


def EjercicioExamen2():
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

Menu()


