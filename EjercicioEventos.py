# #En la empresa XYZ, se realizan mantenimientos preventivos y correctivos,
#  se requiere un programa que registre la fecha de los eventos
# e identificar cual es cual

# Juan Barreto V31106376
import os

#inicio
print("Bienvenido al sistema de la empresa de mantenimiento correctivo y preventivo de la empresa XYZ")
print("En este sistema se pedirá registrar las fechas de los eventos, e identificar cual es cual")
print("Esta identificación se realizará asignando un nombre a cada evento, junto con su fecha")

#inicialización de variables
n=0
listaEventos = []
listaFechas = []

nombre = ""
dia = ""
mes = ""
año = ""
fecha = ""
loop = True

#Primer while que determinará si se siguen añadiendo eventos o no
while(loop == True):
    
    #entrada de datos
    print("Evento n°: ",n+1)
    nombre = input("Ingrese el nombre del evento: ")
    dia = input("Ingrese el día del evento: ")
    mes = input("Ingrese el mes del evento: ")
    año = input("Ingrese el año del evento: ")
    os.system("cls")
    fecha = "("+dia+"/"+mes+"/"+año+")"

    #adicion de eventos a las listas
    listaEventos.append(nombre)
    listaFechas.append(fecha)
    n=n+1

    #Segundo while para asegurarse de que la respuesta de si se desea continuar agregando eventos es correcta o no
    respCont=True
    while respCont==True:
        respuesta = input("¿Desea añadir otro evento?: 1)Si, 2)No")

        if respuesta=="1":
            loop = True
            respCont=False
        elif respuesta=="2":
            loop = False
            respCont=False
        else:
            print("Usted ingresó una respuesta incorrecta, intente de nuevo.")
            respCont=True

#Se muestran los datos almacenados
os.system("cls")
print("***LISTA DE EVENTOS GENERADOS CON SUS FECHAS***")
for i in range(0,n):
    print("*******************")
    print("Evento: ",i+1)
    print("Nombre: ", listaEventos[i])
    print("Fecha: ",listaFechas[i])

doNotStop = input("")


