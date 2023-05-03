import mysql.connector

def delete_table_workflix(table):
    try:
        dataBase = mysql.connector.connect(
            host ="localhost",
            user ="",
            passwd ="",
            database = "workflix"
        )

        cursorObject = dataBase.cursor()
        query = table
        cursorObject.execute(query)
        dataBase.commit()
        print("Se eliminó correctamente la tabla en MySQL")
    except mysql.connector.Error as error:
        print("No se pudo eliminar la tabla en MySQL: {}".format(error))
    finally:
        if dataBase.is_connected():
            dataBase.close()