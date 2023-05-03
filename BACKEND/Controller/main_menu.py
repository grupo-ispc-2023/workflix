import conexion
from fetching_data import list_users_professionals
from functions import insert_data_professional,data_table,update_data,delete_data,remove_table,filter_data_up,order_data_up

def main_menu():
    access = True
    while(access):
        option_correct = False
        while(not option_correct):
            print("==================== MENÚ PRINCIPAL ====================")
            print("1. Probar conexión con el servidor MySQL")
            print("2. Crear nueva tabla")
            print("3. Lista de usuarios profesionales")
            print("4. Ordenar los datos de los usuarios profesionales")
            print("5. Filtrar datos de los usuarios profesionales")
            print("6. Agregar un usuario profesional")
            print("7. Actualizar datos de un usuario profesional")
            print("8. Eliminar un usuario profesional")
            print("9. Eliminar una tabla")
            print("10. Salir")
            print("========================================================")
            option = int(input("Seleccione una opción: "))
            print("")

            if option < 1 or option > 10:
                print("Opción incorrecta, ingrese nuevamente...")
            elif option == 10:
                access = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                option_correct = True
                ejecute_option(option)

def ejecute_option(option):
    if option == 1:
        test_connection = conexion.Connect()
        test_connection.connection_mysql()
    elif option == 2:
        data_table()
    elif option == 3:
        list_users_professionals()
    elif option == 4:
        order_data_up()
    elif option == 5:
        filter_data_up()
    elif option == 6:
        insert_data_professional()
    elif option == 7:
        update_data()
    elif option == 8:
        delete_data()
    elif option == 9:
        remove_table()
    else:
        print("Opción invalida...")

main_menu()