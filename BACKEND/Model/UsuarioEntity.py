from abc import ABC, abstractmethod

class UsuarioEntity(ABC):
    def __init__(self, id, nombre, apellido, email, contrasena, telefono, fotoPerfil, rol, provincia, ciudad):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasena = contrasena
        self._telefono = telefono
        self._fotoPerfil = fotoPerfil
        self._rol = rol
        self._provincia = provincia
        self._ciudad = ciudad

# Getters y Setters
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_apellido(self):
        return self._apellido

    def set_apellido(self, apellido):
        self._apellido = apellido

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_contrasena(self):
        return self._contrasena

    def set_contrasena(self, contrasena):
        self._contrasena = contrasena

    def get_telefono(self):
        return self._telefono

    def set_telefono(self, telefono):
        self._telefono = telefono

    def get_fotoPerfil(self):
        return self._fotoPerfil

    def set_fotoPerfil(self, fotoPerfil):
        self._fotoPerfil = fotoPerfil

    def get_rol(self):
        return self._rol

    def set_rol(self, rol):
        self._rol = rol

    def get_provincia(self):
        return self._provincia

    def set_provincia(self, provincia):
        self._provincia = provincia

    def get_ciudad(self):
        return self._ciudad

    def set_ciudad(self, ciudad):
        self._ciudad = ciudad

