from typing import List
from UsuarioEntity import UsuarioEntity
from UsuarioClienteEntity import UsuarioClienteEntity
from UsuarioProfesionalEntity import UsuarioProfesionalEntity

class UsuarioAdministradorEntity(Usuario):
    def __init__(self, id, nombre, apellido, email, contrasena, telefono, 
    fotoPerfil, rol, provincia, ciudad):
        super().__init__(id, nombre, apellido, email, contrasena, telefono, 
        fotoPerfil, rol, provincia, ciudad)


        
    # Getters y Setters
    def getId(self) -> int:
        return self._id
    
    def setId(self, id: int):
        self._id = id
        
    def getNombre(self) -> str:
        return self._nombre
    
    def setNombre(self, nombre: str):
        self._nombre = nombre
        
    def getApellido(self) -> str:
        return self._apellido
    
    def setApellido(self, apellido: str):
        self._apellido = apellido
        
    def getEmail(self) -> str:
        return self._email
    
    def setEmail(self, email: str):
        self._email = email
        
    def getContrasena(self) -> str:
        return self._contrasena
    
    def setContrasena(self, contrasena: str):
        self._contrasena = contrasena
        
    def getTelefono(self) -> str:
        return self._telefono
    
    def setTelefono(self, telefono: str):
        self._telefono = telefono
        
    def getFotoPerfil(self) -> str:
        return self._fotoPerfil
    
    def setFotoPerfil(self, fotoPerfil: str):
        self._fotoPerfil = fotoPerfil
        
    def getRol(self) -> Rol:
        return self._rol
    
    def setRol(self, rol: Rol):
        self._rol = rol
        
    def getProvincia(self) -> Provincia:
        return self._provincia
    
    def setProvincia(self, provincia: Provincia):
        self._provincia = provincia
        
    def getCiudad(self) -> Ciudad:
        return self._ciudad
    
    def setCiudad(self, ciudad: Ciudad):
        self._ciudad = ciudad












