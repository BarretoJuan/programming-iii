#El siguiente programa se encarga de recibir el input de un usuario y determinar
# si ese input representa o no un numero primo
# para la realizacion de este programa solo se utilizaran condicionales if



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

