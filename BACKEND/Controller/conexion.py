import mysql.connector
from mysql.connector import Error

class Connect:
    def connection_mysql(self):
        try:
            dataBase = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='',
                password='',
                db='workflix'
            )
            print("Conexión correcta")
            db_Info = dataBase.get_server_info()
            print("Conectado a la versión del servidor MySQL", db_Info)
            print(dataBase)
            print("")
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))
        finally:
            if dataBase.is_connected():
                dataBase.close()