#Juan Barreto V31106376
#A continuación se desarrollará una aplicación de cajero automático
#En esta aplicación se creará una cuenta con su nombre titular, y cédula, junto con un saldo inicial

#Una vez creada la cuenta se tienen las funciones de revisar el saldo, añadir fondos a la cuenta y retirar fondos}
import os

#Clase Cuenta
class Cuenta: 
    #Constructor
    def __init__(self, monto):
        self.monto = monto

    #Consultar saldo    
    def ConsultarSaldo(self):
        return self.monto

    #Añadir Fondos
    def AñadirFondos(self, deposito):
        self.deposito = deposito
        self.monto = self.monto + deposito
        return print("Se depositaron", deposito, " Bs.")

    #Retirar Fondos
    def RetirarFondos(self,retiro):
        self.retiro = retiro
        self.monto = self.monto - retiro
        return print("Se retiraron", retiro, " Bs.")

#Inicio
print("Bienvenido/a al sistema de cajero automático de BancoVirtual.")
print("A continuación, usted podrá crear una cuenta en el banco")
print("Y una vez creada, podrá consultar su saldo, ingresar fondos, y retirar fondos de su cuenta")

#Ingreso de datos
nombre = input("Ingrese su nombre completo:  ")
cedula = input("Ingrese su número de cédula: ")
contraseña = input("Ingrese su contraseña para el cajero automático: ")
cantidad = int(input("Ingrese el saldo inicial de apertura de su cuenta, de no desear ingresar un saldo de apertura, ingrese 0: (Montos de Bs.)"))

#se verifica si el monto inicial ingresado es un valor negativo
if (cantidad<0):
    print("No puede ingresar un monto negativo, su monto inicial será 0 Bs.")
    cantidad = 0

#se crea la cuenta
cuenta = Cuenta(cantidad)
os.system("cls")

#Inicio de sesion
e=True
while e == True:
    print("***INICIO DE SESIÓN***")
    cedulaLogin = input("Ingrese la cédula registrada: ")
    contraseñaLogin = input("Ingrese su contraseña: ")
    
    if (cedulaLogin == cedula and contraseñaLogin == contraseña):
        os.system("cls")
        print("Inicio de sesión exitoso")
        e=False

    else:
        os.system("cls")
        print("Credenciales inválidas, intente de nuevo")

#Consultas
start = True
while (start == True):
    print('CAJERO AUTOMÁTICO')
    print("Bienvenido/a: ",nombre)
    print("¿Qué operación desea realizar?")
    print("1) Consultar Saldo")
    print("2) Hacer un depósito")
    print("3) Hacer un retiro")
    print("4) Salir")
    op = int(input(" "))
    #Consulta de saldo
    if (op == 1):
        os.system("cls")
        print("Su saldo actual es de: ",cuenta.ConsultarSaldo(), " Bs.")

    #Depósito, se verifica que el monto no sea negativo
    elif (op ==2):
        
        deposito = int(input("Ingrese el monto a depositar: ")) 
        os.system("cls")
        if (deposito<0):
            print("No puede añadir montos negativos, se depositarán 0 Bs")
            deposito =0
        cuenta.AñadirFondos(deposito)


    elif (op==3):
       
        retiro = int(input("Ingrese el monto a retirar: ")) 
        os.system("cls")
        if (retiro<0):
            print("No puede retirar montos negativos, se retirarán 0 Bs")
            retiro =0
        elif(retiro>cuenta.ConsultarSaldo()):
            print("No tiene saldo suficiente para realizar el retiro")
            retiro =0
        cuenta.RetirarFondos(retiro)


    elif (op==4):
        os.system("cls")
        print("Gracias por usar nuestros servicios")
        start = False
        
    else:
        os.system("cls")
        print("Usted ingresó una operación inválida")
    
doNotEnd = input("")