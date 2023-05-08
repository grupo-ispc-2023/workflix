class ServicioEntity:
    def __init__(self, id: int, nombre: str, usuarioProfesional: UsuarioProfesional):
        self._id = id
        self._nombre = nombre
        self._usuarioProfesional = usuarioProfesional
    
    # Getters y setters
    def getId(self) -> int:
        return self._id
    
    def setId(self, id: int):
        self._id = id
        
    def getNombre(self) -> str:
        return self._nombre
    
    def setNombre(self, nombre: str):
        self._nombre = nombre
    
    def getUsuarioProfesional(self) -> UsuarioProfesional:
        return self._usuarioProfesional
    
    def setUsuarioProfesional(self, usuarioProfesional: UsuarioProfesional):
        self._usuarioProfesional = usuarioProfesional
