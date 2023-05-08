import mysql.connector

def list_users_professionals():
    try:
        dataBase = mysql.connector.connect(
            host ="localhost",
            user ="",
            passwd ="",
            database = "workflix"
        )

        cursorObject = dataBase.cursor()
        
        query = "SELECT id, nombre, apellido, email, contrasena, foto_perfil, telefono, localidad, provincia, profesion, descripcion, calificacion_obtenida FROM usuarios_profesionales"
        cursorObject.execute(query)
        
        myresult = cursorObject.fetchall()
        for x in myresult:
            print(x)

        print("")
    except mysql.connector.Error as error:
        print("Error al intentar obtener datos de MySQL: {}".format(error))
    finally:
        if dataBase.is_connected():
            dataBase.close()