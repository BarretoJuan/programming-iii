#El siguiente programa se encarga de recibir el input de un usuario y determinar
# si ese input representa o no un numero primo
# para la realizacion de este programa solo se utilizaran condicionales if

num = int(input("Ingrese un numero para determinar si es o no un numero primo: "))

#Se verifica si el numero ingresado es 0 o 1
if(num == 0 or num ==1 ):
    print(num, " no es primo")
#Se verifica si el numero ingresado es alguno de los 4 menores numeros primos
elif(num==2 or num==3 or num==5 or num==7):
    print(num, " es primo")
#De ser divisible entre alguno de los cuatro menores numeros primos, se considera no primo
elif(num%2==0 or num%3==0 or num%5==0 or num%7==0):
    print(num, " no es primo")
#De lo contrario, es primo
else:
    print(num, " es primo")
