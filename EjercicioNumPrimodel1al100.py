#El siguiente programa se encarga de recibir el input de un usuario y determinar
# si ese input representa o no un numero primo
# para la realizacion de este programa solo se utilizaran condicionales if


list = []

for i in range(0,101):
    #Se verifica si el numero ingresado es 0 o 1
    if(i == 0 or i ==1 ):
        i=i
    #Se verifica si el numero ingresado es alguno de los 4 menores numeros primos
    elif(i==2 or i==3 or i==5 or i==7):
        list.append(i)
    #De ser divisible entre alguno de los cuatro menores numeros primos, se considera no primo
    elif(i%2==0 or i%3==0 or i%5==0 or i%7==0):
        i=i
    #De lo contrario, es primo
    else:
        list.append(i)

for i in range(0,len(list)):
      print(list[i])
