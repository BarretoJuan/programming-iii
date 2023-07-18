# #En el siguiente programa se implementarán un sistema CRUD para una base de datos de una relacion
# #Un sistema CRUD permite:
# Create (Crear) datos en una base de datos
# Read (Leer) datos en una base de datos
# Update (Actualizar) datos en una base de datos
# Delete (Eliminar) datos en una base de datos

# La base de datos a implementar es una tabla de estudiantes con los siguientes atributos:

# +------------------+--------------+------+-----+---------+-------+
# | Field            | Type         | Null | Key | Default | Extra |
# +------------------+--------------+------+-----+---------+-------+
# | nombre           | varchar(45)  | NO   |     | NULL    |       |
# | cedula           | int(12)      | NO   | UNI | NULL    |       |
# | fecha_nacimiento | date         | YES  |     | NULL    |       |
# | direccion        | text         | YES  |     | NULL    |       |
# | email            | varchar(45)  | NO   | UNI | NULL    |       |
# | id               | int(10)      | NO   | PRI | NULL    |       |
# | carrera          | varchar(100) | NO   |     | NULL    |       |
# | telefono         | varchar(45)  | NO   | UNI | NULL    |       |
# +------------------+--------------+------+-----+---------+-------+

#Se importa la libreria pymysql
import pymysql

#Create
def insertar_usuario(nombre, cedula, fecha_nacimiento, direccion, email, carrera, telefono):
    query = """
            INSERT INTO estudiante VALUES (%s, %s, %s, %s, %s, %s, %s, NULL);
            """
    cursor.execute(query, (nombre, cedula, fecha_nacimiento, direccion, email, carrera, telefono,))
    connection.commit()
    print("Inserción exitosa")

#Read
def leer_usuarios():
    query = """
            SELECT * FROM estudiante;
            """
    cursor.execute(query)
    output = cursor.fetchall()
    print(output)

#Update
def actualizar_usuario(nombre, fecha_nacimiento, direccion, email, carrera, telefono, cedula):
    query = """
            UPDATE ESTUDIANTE
            SET NOMBRE = %s,
            FECHA_NACIMIENTO = %s,
            DIRECCION = %s,
            EMAIL = %s,
            CARRERA = %s,
            TELEFONO = %s
            WHERE CEDULA = %s;

            """
    cursor.execute(query, (nombre, fecha_nacimiento, direccion, email, carrera, telefono, cedula,))
    connection.commit()
    print("Actualizacion exitosa")

#Delete
def borrar_usuario(cedula):
    query = """
            DELETE FROM estudiante WHERE cedula = %s;
            """
    cursor.execute(query, (cedula,))
    connection.commit()
    print("Borrado Exitoso")

# Se establece la conexión con la base de datos y se instancia un cursor para ejecutar consultas
connection = pymysql.connect(host='localhost',
                             user='root',
                             database='escuela_urbe',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

cursor.execute("SELECT * FROM ESTUDIANTE")
lista_estudiantes = cursor.fetchall()
print(lista_estudiantes)

respuesta=0
while(respuesta != '5'):
    print("SISTEMA CRUD PARA ESCUELA: ")
    print("1) Insertar Registros ")
    print("2) Leer registros")
    print("3) Actualizar registros")
    print("4) Borrar Registros")
    print("5) Salir")
    respuesta = input("")
    
    if(respuesta == "1"):

        nombre = input("Ingrese el nombre del nuevo estudiante: ")
        while len(nombre) > 45:
            print("El nombre no debe exceder los 45 caracteres.")
            nombre = input("Ingrese el nombre del nuevo estudiante: ")
            existe=False
            cursor.execute ("SELECT * FROM estudiante WHERE cedula = %s", (cedula))
            existe = cursor.fetchone()
            if existe:
                print("Esta cedula ya está registrada con otro usuario")
                existe = True


        cedula = input("Ingrese la cedula del nuevo estudiante: ")
        cursor.execute ("SELECT * FROM estudiante WHERE cedula = %s", (cedula))
        existe = cursor.fetchone()
        while existe or (not cedula.isdigit() or len(cedula) > 12):
            cursor.execute ("SELECT * FROM estudiante WHERE cedula = %s", (cedula))
            existe = cursor.fetchone()
            if existe:
                print("Esta cedula ya está registrada con otro usuario")
                cedula = input("Ingrese la cedula del nuevo estudiante: ")
            while not cedula.isdigit() or len(cedula) > 12:
                print("La cedula debe ser un número entero y no debe exceder los 12 dígitos.")
                cedula = input("Ingrese la cedula del nuevo estudiante: ")
                existe = True


        fecha_nacimiento = input("Ingrese la fecha de nacimiento del nuevo estudiante (año-mes-día): ")
        while len(fecha_nacimiento) != 10 or not fecha_nacimiento[0:3].isdigit() or not fecha_nacimiento[5:6].isdigit() or not fecha_nacimiento[8:9].isdigit() or fecha_nacimiento[4] != '-' or fecha_nacimiento[7] != '-':
            print("El formato de la fecha de nacimiento debe ser 'año-mes-día', ejemplo: 2004-07-09.")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del nuevo estudiante (año-mes-día): ")
    

        direccion = input("Ingrese la dirección del nuevo estudiante: ")


        email = input("Ingrese el email del nuevo estudiante: ")
        cursor.execute ("SELECT * FROM estudiante WHERE email = %s", (email,))
        existe = cursor.fetchone()
        while existe or len(email) > 45:
            cursor.execute ("SELECT * FROM estudiante WHERE email = %s", (email,))
            existe = cursor.fetchone()
            if existe:
                print("Este email ya está registrado con otro usuario")
                existe = True
                email = input("Ingrese el email del nuevo estudiante: ")
            while len(email) > 45:
                print("El email no debe exceder los 45 caracteres.")
                email = input("Ingrese el email del nuevo estudiante: ")
                existe = True
            
    
        carrera = input("Ingrese la carrera del estudiante: ")
        while len(carrera) > 45:
            print("La carrera no debe exceder los 45 caracteres.")
            carrera = input("Ingrese la carrera del estudiante: ")
        

        telefono = input("Ingrese el telefono del nuevo estudiante: (telefono de Venezuela, 11 dígitos, ejemplo: 04145552055) ")
        cursor.execute ("SELECT * FROM estudiante WHERE telefono = %s", (telefono))
        existe = cursor.fetchone()
        while existe or (len(telefono) != 11 or not telefono.isdigit()):
            cursor.execute ("SELECT * FROM estudiante WHERE telefono = %s", (telefono))
            existe = cursor.fetchone()
            if existe:               
                print("Este telefono ya está registrado con otro usuario")
                telefono = input("Ingrese el telefono del nuevo estudiante: ")
            while len(telefono) != 11 or not telefono.isdigit():
                print("El telefono ingresado debe ser un numero y debe contar con 11 digitos (telefono venezolano, ejemplo 04146568915)")
                telefono = input("Ingrese el telefono del nuevo estudiante: ")

        insertar_usuario(nombre, cedula, fecha_nacimiento, direccion, email, carrera, telefono)

    elif(respuesta == "2"):
        leer_usuarios()

    elif(respuesta == "3"):
        cedula = input("Ingrese la cedula del estudiante cuyos datos desea modificar: ")
        cursor.execute("""SELECT * FROM ESTUDIANTE WHERE CEDULA = %s""",(cedula,))
        estudiante = cursor.fetchone()

        if estudiante:
            print("Modificando los datos del estudiante: ",estudiante["nombre"], "(Cédula: ",estudiante["cedula"],")")
            nombre = input("Ingrese el nombre del estudiante: ")
            while len(nombre) > 45:
                print("El nombre no debe exceder los 45 caracteres.")
                nombre = input("Ingrese el nombre del estudiante: ")
                existe=False
                cursor.execute ("SELECT * FROM estudiante WHERE cedula = %s", (cedula))
                existe = cursor.fetchone()
                if existe:
                    print("Esta cedula ya está registrada con otro usuario")
                    existe = True


            fecha_nacimiento = input("Ingrese la fecha de nacimiento del estudiante (año-mes-día): ")
            while len(fecha_nacimiento) != 10 or not fecha_nacimiento[0:3].isdigit() or not fecha_nacimiento[5:6].isdigit() or not fecha_nacimiento[8:9].isdigit() or fecha_nacimiento[4] != '-' or fecha_nacimiento[7] != '-':
                print("El formato de la fecha de nacimiento debe ser 'año-mes-día', ejemplo: 2004-07-09.")
                fecha_nacimiento = input("Ingrese la fecha de nacimiento del estudiante (año-mes-día): ")
        

            direccion = input("Ingrese la dirección del estudiante: ")


            email = input("Ingrese el email del estudiante: ")
            cursor.execute ("SELECT * FROM estudiante WHERE email = %s", (email,))
            existe = cursor.fetchone()
            while existe or len(email) > 45:
                cursor.execute ("SELECT * FROM estudiante WHERE email = %s", (email,))
                existe = cursor.fetchone()
                if existe:
                    print("Este email ya está registrado con otro usuario")
                    existe = True
                    email = input("Ingrese el email del estudiante: ")
                while len(email) > 45:
                    print("El email no debe exceder los 45 caracteres.")
                    email = input("Ingrese el email del estudiante: ")
                    existe = True
                
        
            carrera = input("Ingrese la carrera del estudiante: ")
            while len(carrera) > 45:
                print("La carrera no debe exceder los 45 caracteres.")
                carrera = input("Ingrese la carrera del estudiante: ")
            

            telefono = input("Ingrese el telefono del estudiante: (telefono de Venezuela, 11 dígitos, ejemplo: 04145552055) ")
            cursor.execute ("SELECT * FROM estudiante WHERE telefono = %s", (telefono))
            existe = cursor.fetchone()
            while existe or (len(telefono) != 11 or not telefono.isdigit()):
                cursor.execute ("SELECT * FROM estudiante WHERE telefono = %s", (telefono))
                existe = cursor.fetchone()
                if existe:               
                    print("Este telefono ya está registrado con otro usuario")
                    telefono = input("Ingrese el telefono del estudiante: ")
                while len(telefono) != 11 or not telefono.isdigit():
                    print("El telefono ingresado debe ser un numero y debe contar con 11 digitos (telefono venezolano, ejemplo 04146568915)")
                    telefono = input("Ingrese el telefono del estudiante: ")
            
            actualizar_usuario(nombre, fecha_nacimiento, direccion, email, carrera, telefono, cedula)

        else: 
            print("No se encontró un estudiante con la cedula ingresada")
        
        

    elif(respuesta == "4"):
        cedula = input("Ingrese la cedula del estudiante que desea eliminar: ")
        while not cedula.isdigit() or len(cedula) > 12:
            print("La cedula debe ser un número entero y no debe exceder los 12 dígitos.")
            cedula = input("Ingrese la cedula del estudiante que desea eliminar:  ")
        cursor.execute("SELECT * FROM estudiante WHERE cedula = %s;", (cedula,))
        estudiante = cursor.fetchone()
        if estudiante:
            print("Está seguro que desea eliminar el registro de: ",estudiante["nombre"],"?")
            respuesta = input("1) Sí 2) No: ")
            if(respuesta == 1):
                borrar_usuario(cedula)
                print("Borrado exitoso")
        else:
            print("No se encontró un estudiante con la cedula suministrada.")
    

    elif(respuesta == "5"):
        print("Gracias, que tenga un buen día")
        connection.close()
    else:
        print("Respuesta no válida")



