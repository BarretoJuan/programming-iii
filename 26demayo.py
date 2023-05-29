# el ciclo for
# TAREA AÑADIR AL EJERCICIO DE LA PANADERIA, PARA AÑADIR UN DESCUENTO SEGUN PAIS
# 
# 
# 
# 

# for i in range(1,50):
#         print("hola numero ",i )


# 
# myarray = [1,7,3,9]
 
# test = list("4555")hola
# print(test)
# mrarray = range(1,10)


# help(object)

# for i in mrarray:
#         print("hola... ", i)


paisesYCapitales = {
                    "Antigua y Barbuda":"St John",
                    "Argentina": "Buenos Aires",
                    "Bahamas":"Nassau",
                    "Barbados":"Bridgetown",
                    "Belice":"Belmopan",
                    "Bolivia":"Sucre",
                    "Brasil":"Brasilia",
                    "Canada":"Ottawa",
                    "Chile":"Santiago",
                    "Colombia":"Bogota",
                    "Costa Rica":"San José",
                    "Cuba":"Havana",
                    "Dominica":"Roseau",
                    "República Dominicana":"Santo Domingo",
                    "Ecuador":"Quito",
                    "El Salvador":"San Salvador",
                    "Granada":"St. George",
                    "Guatemala":"Guatemala",
                    "Guyana":"Georgetown",
                    "Haití":"Puerto Principe",
                    "Honduras":"Tegucigalpa",
                    "Jamaica":"Kingston",
                    "México":"Mexico City",
                    "Nicaragua":"Managua",
                    "Panamá":"Panama City",
                    "Paraguay":"Asuncion",
                    "Perú":"Lima",
                    "San Cristóbal y Nieves":"Basseterre",
                    "Santa Lucía":"Castries",
                    "San Vicente y Granadinas":"Kinggstown",
                    "Suriname":"Paramaribo",
                    "Trinidad y Tobago":"Puerto España",
                    "Estados Unidos":"Washington",
                    "Uruguay":"Montevideo",
                    "Venezuela":"Caracas",
                    }

paisInput = str(input("Ingrese un pais de america: "))
paisExiste=0


for i in paises:
    if (paisInput == i):
        paisExiste=paisExiste+1
      
 
if(paisExiste==1):
    print("El pais ",paisInput," Sí existe en America y su capital es:",
           paisesYCapitales[paisInput])

else:
    print("El pais ",paisInput," No existe en America")
