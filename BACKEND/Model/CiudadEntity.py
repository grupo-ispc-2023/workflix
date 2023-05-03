class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre

    # Getters y Setters
    def getId(self) -> int:
        return self._id
    
    def setId(self, id: int):
        self._id = id
        
    def getNombre(self) -> str:
        return self._nombre
    
    def setNombre(self, nombre: str):
        self._nombre = nombre
        
    def getProvincia(self) -> Provincia:
        return self._provincia
    
    def setProvincia(self, provincia: Provincia):
        self._provincia = provincia