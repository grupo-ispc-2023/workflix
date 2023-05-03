import mysql.connector

def filter_data_users_professionals(data):
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
        myresult = cursorObject.fetchall()
        for x in myresult:
            print(x)
        
        print("")
    except mysql.connector.Error as error:
        print("Error al intentar filtrar datos de los usuarios profesionales: {}".format(error))
    finally:
        if dataBase.is_connected():
            dataBase.close()