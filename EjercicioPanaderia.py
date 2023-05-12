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