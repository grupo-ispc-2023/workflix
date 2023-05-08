import mysql.connector

def new_table(data):
    try:
        dataBase = mysql.connector.connect(
            host ="localhost",
            user ="",
            passwd ="",
            database = "workflix"
        )
        cursorObject = dataBase.cursor()
        newTable = data
        cursorObject.execute(newTable)
        print("Tabla creada con exito!")
    except mysql.connector.Error as error:
        print("No se pudo crear la tabla en MySQL: {}".format(error))
    finally:
        if dataBase.is_connected():
            dataBase.close()