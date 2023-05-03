import mysql.connector

def delete_data_professional(data):
    try:
        dataBase = mysql.connector.connect(
            host ="localhost",
            user ="",
            passwd ="",
            database = "workflix"
        )
        cursorObject = dataBase.cursor()
        query = data
        cursorObject.execute(query)
        dataBase.commit()
        print(cursorObject.rowcount, "registro(s) borrado\n") 
    except mysql.connector.Error as error:
        print("No se pudo eliminar el registro de la tabla en MySQL: {}".format(error))
    finally:
        if dataBase.is_connected():
            dataBase.close()