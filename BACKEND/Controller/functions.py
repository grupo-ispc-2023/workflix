from create_table import new_table
from delete_data_table import delete_data_professional
from delete_table import delete_table_workflix
from insert_data_single_row import insert_data_single_professional_mysql
from filter_data import filter_data_users_professionals
from order_data import order_data_user_professionals
from update_data import modify_data_professional

def insert_data_professional():
    print("Ingrese los siguientes datos del usuario profesional\n")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    contrasena = input(str("Contraseña: "))
    foto_perfil = input("Foto de perfil (link): ")
    telefono = input(str("Teléfono: "))
    localidad = input("Localidad: ")
    provincia = input("Provincia: ")
    profesion = input("Profesión: ")
    descripcion = input("Descripción: ")
    calificacion_obtenida = float(input("Calificación obtenida: "))
    insert_data_single_professional_mysql(nombre, apellido, email, contrasena, foto_perfil, telefono, localidad, provincia, profesion, descripcion, calificacion_obtenida)

def data_table():
    name_table = input("Nombre de la tabla: ")
    c1 = input("Columna 1: ")
    t1 = input("Tipo de dato 1: ")
    r1 = input("Restricción 1: ")
    c2 = input("Columna 2: ")
    t2 = input("Tipo de dato 2: ")
    r2 = input("Restricción 2: ")
    c3 = input("Columna 3: ")
    t3 = input("Tipo de dato 3: ")
    r3 = input("Restricción 3: ")
    d_table = "CREATE TABLE " + name_table + "(" + c1 + " " + t1 + " " + r1 + "," + c2 + " " + t2 + " " + r2 + "," + c3 + " " + t3 + " " + r3 + ")"
    new_table(d_table)

def update_data():
    u_set = input("Ingrese la cláusula SET: ")
    u_where = input("Ingrese la cláusula WHERE: ")
    d_professional = "UPDATE usuarios_profesionales SET " + u_set + " " + "WHERE " + u_where
    modify_data_professional(d_professional)

def delete_data():
    d_where = input("Ingrese la cláusula WHERE: ")
    d_data = "DELETE FROM usuarios_profesionales WHERE " + d_where
    delete_data_professional(d_data)

def remove_table():
    r_where = input("Ingrese en nombre de la tabla: ")
    r_table = "DROP TABLE " + r_where + ";"
    delete_table_workflix(r_table)

def filter_data_up():
    f_where = input("Ingrese la cláusula WHERE: ")
    f_data = "SELECT * FROM usuarios_profesionales WHERE " + f_where
    print(" ")
    filter_data_users_professionals(f_data)

def order_data_up():
    o_order = input("Ingrese la cláusula ORDER BY: ")
    o_data = "SELECT * FROM usuarios_profesionales ORDER BY " + o_order
    order_data_user_professionals(o_data)