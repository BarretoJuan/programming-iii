

# La pizzeria bella napoli ofrece pizzas vegetarianas y no
# vegetarianas a sus clientes. Los ingredientes para cada
# tipo de pizza aparecen a continuación:

# Ingredientes vegetarianos: pimiento y tofu
# Ingredientes no vegetarianos: peperoni, jamon y salmon.

# Escribir un programa que pregunte al usuario si quiere 
# una pizza vegetariana o no, y en funcion de la respuesta
# le muestre un menú con los ingredientes disponibles para
# que elija. Solo se puede elegir un ingrediente además de
# la mozzarella, y el tomate que están en todas las pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida es
# vegetariana o no y todos los ingredientes que lleva

#declaracion de tuplas
ingredientesVegetarianos = ("Pimiento", "Tofu")
ingredientesNoVegetarianos = ("Peperoni", "Jamón", "Salmón")


#inicio
print("Bienvenido/a a la Pizzeria Bella Napoli, contamos con menú vegetariano y no vegetariano")
print("Todas nuestras pizzas incluyen mozzarella y tomate")

#loop while para determinar el tipo de pizza
loop=True
while loop==True:

    tipoPizzaEntrada = input("Desea una pizza vegetariana? 1)Si 2)No:")

    if(tipoPizzaEntrada == "1"):
        isVegetariana = True
        loop = False
        print("Perfecto! se le mostrará un menú vegetariano")

    elif(tipoPizzaEntrada == "2"):
        isVegetariana = False
        loop = False
        print("Perfecto! se le mostrará un menú no vegetariano")

    else:
        print("Respuesta no válida, intente de nuevo")

print("Ingrese el ingrediente a elegir de su pizza: ")

#escoger pizza vegetariana
if(isVegetariana):
    print("**Ingredientes**")
    i = 0
    for i in ingredientesVegetarianos:
        print(i)
    print("**********")
    

    loop2 = True
    while loop2==True:
        ingrediente = input("Seleccione su ingrediente de la lista: ")
        ingredienteExiste=False
        for i in ingredientesVegetarianos:  
            if(ingrediente == i):
                ingredienteExiste =True
                loop2=False
        if(ingredienteExiste ==False):
            print("Usted ingresó un ingrediente invalido, intente de nuevo")
        
    print("Usted seleccionó una pizza vegetariana de ingrediente: ",ingrediente, ", Tomate, y Mozarella")

#escoger pizza no vegetariana
elif(isVegetariana==False):
    print("**Ingredientes**")
    i = 0
    for i in ingredientesNoVegetarianos:
        print(i)
    print("**********")
    

    loop2 = True
    while loop2==True:
        ingrediente = input("Seleccione su ingrediente de la lista: ")
        ingredienteExiste=False
        for i in ingredientesNoVegetarianos:  
            if(ingrediente == i):
                ingredienteExiste =True
                loop2=False
        if(ingredienteExiste ==False):
            print("Usted ingresó un ingrediente invalido, intente de nuevo")
        
    print("Usted seleccionó una pizza NO vegetariana de ingredientes: ",ingrediente, ", Tomate, y Mozarella")

doNotEndUnexpectedly = input("")

    
