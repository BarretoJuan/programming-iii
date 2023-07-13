# Unidad 3: Bases de adtos y validació
# en la escuela maria chiquinquira, tiene una matricula de 637 estudiantes  
# cuenta con 12 salones con capacidad de 30 estudiantes cada uno
#  la escuela trabaja dos turnos, mañana y tarde
# 
# Realizar un programa que acomode cada estudiante en cada aula, en los dos turnos
# Juan Barreto V31106376    

print("En la escuela Maria Chiquinquirá tenemos 12 salones disponibles, y un turno en la mañana y en la noche")
print("Cada salon tiene una capacidad de 30 estudiantes")
print("Se tiene una matricula total de 637 estudiantes")
print("Se dividen 318 estudiantes en la mañana")
print("Se dividen 319 estudiantes en la tarde")
print("Se genera la disposición de estudiantes en cada turno: ")

#se inicializan las variables
print("")
print("*****************")
print("TURNO DE MAÑANA:")
capManana=318
capMananaRestante = capManana
capTarde = 319
capTardeRestante = capTarde
capSalon = 30

#ciclo for para llenar el turno de la manana

for i in range(1,13):
    #Si la capacidad restante de estudiantes es suficiente para llenar un salon, el salon en cuestion tendra capacidad llena
    if (capMananaRestante>=30):
        print("salon ",i,": capacidad ",capSalon,"/",capSalon)
        capMananaRestante = capMananaRestante-capSalon
    
    #Si la capacidad restante es 0, el salon en cuestion estará vacío, pues ya se asignó un salon a cada alumno del turno
    elif(capMananaRestante<=0):
        print("salon ",i,": capacidad 0/",capSalon)

    #de lo contrario, es decir si el remanente de estudiantes es positivo, pero no suficiente para llenar un salon a su capacidad maxima
    #se llena el salon restante hasta donde se pueda
    else:
        print("salon: ",i," capacidad ",capMananaRestante,"/",capSalon)
        capMananaRestante = capMananaRestante-capSalon

print("")
print("*****************")
print("TURNO DE TARDE: ")

#ciclo for para llenar el turno de la noche
for i in range(1,13):
    #Si la capacidad restante de estudiantes es suficiente para llenar un salon, el salon en cuestion tendra capacidad llena
    if (capTardeRestante>=30):
        print("salon ",i,": capacidad ",capSalon,"/",capSalon)
        capTardeRestante = capTardeRestante-capSalon

     #Si la capacidad restante es 0, el salon en cuestion estará vacío, pues ya se asignó un salon a cada alumno del turno
    elif(capTardeRestante<=0):
        print("salon ",i,": capacidad 0/",capSalon)

    #de lo contrario, es decir si el remanente de estudiantes es positivo, pero no suficiente para llenar un salon a su capacidad maxima
    #se llena el salon restante hasta donde se pueda
    else:
        print("salon: ",i," capacidad ",capTardeRestante,"/",capSalon)
        capTardeRestante = capTardeRestante-capSalon