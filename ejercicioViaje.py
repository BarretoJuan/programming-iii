# la empresa de viajes maduro tours cuenta con 4 paquetes
# *** bronce: Cumaná 4 noche y 3 dias
#  200$ por persona, incluye un viaje a la selva, 
# el servicio de transporte cuesta 20$
# *** plata: Margarita 7 dias y 6 noches por 300$ por persona persona,
#  el transporte cuesta
# 50$
#  *** oro: LOS CAYOS VAMOO, 7 dias y 6 noches 500$, ese no tiene transporte
#  *** Platino: isla las aves, 3 dias y 2 noches 1000$, ese no tiene transporte
#  *** Diamante: Los Roques, 10 dias y 9 noches 5000$, yate incluido, todo incluido
# hacer un sistema de agendas

# juan barreto v31106376


import os
import datetime


#while para verificar que se ingrese una entrada valida
resp =True
while resp==True:

#se muestran los datos
    print("Bienvenido a la empresa de viajes Maduro Tours, nuestra empresa cuenta con 4 paquetes: ")
    print(" ")
    print("1. Paquete Bronce: Viaje a Cumaná, 4 noches y 3 días, 200$ por persona, el servicio de transporte opcional tiene un costo de 20$")
    print(" ")
    print("2. Paquete Plata: Viaje a Margarita, 7 dias y 6 noches, 300$ por persona, el servicio de transporte opcional tiene un costo de 50$")
    print(" ")
    print("3. Oro: Viaje a Los Cayos. 7 días y 6 noches, 500$ por persona, no hay servicio de transporte")
    print(" ")
    print("4. Platino: Viaje a Isla Las Aves, 3 días y 2 noches, 1000$ por persona, no hay servicio de transporte")
    print(" ")
    print("5. Diamante: Los Roques, 10 dias y 9 noches, 5000$ por persona, servicio de yate incluído")
    print(" ")

#entrada de datos de paquetes y numero de personas
    respuesta = input("Ingrese el paquete que desea agendar: ")
    numPersonas = int(input("Ingrese el numero de personas a agendar en el  paquete: "))

#ifs para paquetes, se estbalecen las variables, se pregunta por la contratacion de transporte en caso de aplicarse, y se establece una fecha de salida para el día siguiente, y una fecha de retorno acorde al numero de dias del paquete
    if (respuesta == "1"):
        catPaquete = "Bronce"
        destino = "Cumaná"
        duracion = "4 noches y 3 días"
        precioPPersona = 200

        fechaActual = datetime.date.today()
        fechaIda = fechaActual + datetime.timedelta(days=1)
        fechaVuelta = fechaIda + datetime.timedelta(days=4)

        fechaIdaFormato = fechaIda.strftime("%d/%m/%y")
        fechaVueltaFormato = fechaVuelta.strftime("%d/%m/%y")

        deseaTransporte = input("Desea contratar el servicio de transporte de 20$?: 1)Si, 2)No")
        if deseaTransporte == "1":
            transporte = 20
        else:
            transporte = 0
        precio = numPersonas*precioPPersona+transporte
        resp = False
            
        

    elif (respuesta =="2"):
        catPaquete = "Plata"
        destino = "Margarita"
        duracion = "7 días y 6 noches"
        precioPPersona =300

        fechaActual = datetime.date.today()
        fechaIda = fechaActual + datetime.timedelta(days=1)
        fechaVuelta = fechaIda + datetime.timedelta(days=7)

        fechaIdaFormato = fechaIda.strftime("%d/%m/%y")
        fechaVueltaFormato = fechaVuelta.strftime("%d/%m/%y")

        deseaTransporte = input("Desea contratar el servicio de transporte de 20$?: 1)Si, 2)No")
        if deseaTransporte == "1":
            transporte = 50
        else:
            transporte = 0
        precio = numPersonas*precioPPersona+transporte
        resp = False
            

    elif (respuesta =="3"):
        catPaquete = "Oro"
        destino = "Los Cayos"
        duracion = "7 días y 6 noches"
        precioPPersona =500
        transporte = 0
        precio = numPersonas*precioPPersona+transporte
        resp = False

        fechaActual = datetime.date.today()
        fechaIda = fechaActual + datetime.timedelta(days=1)
        fechaVuelta = fechaIda + datetime.timedelta(days=7)

        fechaIdaFormato = fechaIda.strftime("%d/%m/%y")
        fechaVueltaFormato = fechaVuelta.strftime("%d/%m/%y")


    elif (respuesta =="4"):
        catPaquete = "Platino"
        destino = "Isla las Aves"
        duracion = "3 días y 2 noches"
        precioPPersona =1000
        transporte = 0
        precio = numPersonas*precioPPersona+transporte
        resp = False

        fechaActual = datetime.date.today()
        fechaIda = fechaActual + datetime.timedelta(days=1)
        fechaVuelta = fechaIda + datetime.timedelta(days=3)

        fechaIdaFormato = fechaIda.strftime("%d/%m/%y")
        fechaVueltaFormato = fechaVuelta.strftime("%d/%m/%y")

    elif (respuesta =="5"):
        catPaquete = "Diamante"
        destino = "Los Roques"
        duracion = "10 días y 9 noches"
        precioPPersona =5000
        transporte = 0
        precio = numPersonas*precioPPersona+transporte    
        resp = False


        fechaActual = datetime.date.today()
        fechaIda = fechaActual + datetime.timedelta(days=1)
        fechaVuelta = fechaIda + datetime.timedelta(days=10)

        fechaIdaFormato = fechaIda.strftime("%d/%m/%y")
        fechaVueltaFormato = fechaVuelta.strftime("%d/%m/%y")


    else:
        os.system("CLS")
        print("Ingresó un número de paquete inválido, intente de nuevo")

#Se muestran los datos
print("****VIAJE AGENDADO:**** ")
print("Categoría del paquete: ",catPaquete)
print("Destino: ",destino)
print("Duración: ",duracion)   
print("Número de personas: ",numPersonas)
print("Precio por persona: ", precioPPersona,"$")
print("Precio por transporte: ",transporte,"$")
print("Precio total a pagar: ",precio,"$")
print("")
print("FECHA DE SALIDA: ",fechaIdaFormato)
print("FECHA DE RETORNO: ",fechaVueltaFormato)