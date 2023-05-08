import mysql.connector

try: 
    dataBase = mysql.connector.connect(
        host="localhost",
        user="",
        passwd="",
        database="workflix"
    )

    cursorObject = dataBase.cursor()

    sql = "INSERT INTO usuarios_profesionales (nombre, apellido, email, contrasena, foto_perfil, telefono, localidad, provincia, profesion, descripcion, calificacion_obtenida)\
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = [("juan", "perez", "jp@gmail.com", "admin", "fotourljp.imagen.com", "3515644868", "Cordoba", "Cordoba",
            "electricista", "", 7),
        ("Pablo", "garay", "pg@gmail.com", "root", "fotourlpg.imagen.com", "3515644861", "Villa Maria", "Cordoba",
            "gasista", "", 6),
        ("Emiliano", "Rodriguez", "er@gmail.com", "admin", "fotourl.imagen.com", "3515644862", "Capital", "Buenos Aires",
            "plomero", "", 7)]

    cursorObject.executemany(sql, val)
    dataBase.commit()
except mysql.connector.Error as error:
        print("No se pudo agregar el registro en la tabla de MySQL: {}".format(error))
finally:
    if dataBase.is_connected():
        dataBase.close()