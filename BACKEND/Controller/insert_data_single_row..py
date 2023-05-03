import mysql.connector

def insert_data_single_professional_mysql(nombre, apellido, email, contrasena, foto_perfil, telefono, localidad, provincia, profesion, descripcion, calificacion_obtenida):
    try:
        dataBase = mysql.connector.connect(
            host ="localhost",
            user ="",
            passwd ="",
            database = "workflix"
        )
      
        cursorObject = dataBase.cursor()
        data_professional = (nombre, apellido, email, contrasena, foto_perfil, telefono, localidad, provincia, profesion, descripcion, calificacion_obtenida)
        sql = ('INSERT INTO usuarios_profesionales(nombre, apellido, email, contrasena, foto_perfil, telefono, localidad, provincia, profesion, descripcion, calificacion_obtenida)'
        'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)')
        cursorObject.execute(sql,data_professional)
        dataBase.commit()
        print("Se agrego con exitó el usuario profesional " + nombre + " " + apellido + " en MySQL\n")
    except mysql.connector.Error as error:
        print("No se pudo agregar el registro en la tabla de MySQL: {}".format(error))
    finally:
        if dataBase.is_connected():
            dataBase.close()

