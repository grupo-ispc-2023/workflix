import mysql.connector

def order_data_user_professionals(data):
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
      print("No se pudo ordenar los registros de la tabla: {}".format(error))
  finally:
      if dataBase.is_connected():
          dataBase.close()