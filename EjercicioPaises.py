# # JUAN BARRETO 31106376 
# PROGRAMACION 3 N-613 
#Se pregunta al usuario por un pais de america, y si existe, se muestra su capital

#diccionario de paises
paises = {
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
#entrada del pais
paisInput = str(input("Ingrese un pais de america: "))
paisExiste=0

#for para determinar si el pais existe
for i in paises:
    if (paisInput == i):
        paisExiste=paisExiste+1
      
 #salida de datos
if(paisExiste==1):
    print("El pais ",paisInput," Sí existe en America y su capital es:",
           paises[paisInput])

else:
    print("El pais ",paisInput," No existe en America")
