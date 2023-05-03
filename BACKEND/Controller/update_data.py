import mysql.connector

def modify_data_professional(data):
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
      print("Se actualizo con exitó los datos en MySQL\n")
  except mysql.connector.Error as error:
    print("No se pudo actualizar los datos del usuario profesional en MySQL {}".format(error))
  finally:
      if dataBase.is_connected():
          dataBase.close()