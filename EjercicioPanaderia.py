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