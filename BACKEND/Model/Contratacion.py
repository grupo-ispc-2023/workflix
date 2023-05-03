class ContratacionEntity:
    def __init__(self, id: int, fecha: str, valoracion: float, comentario: str, factura: Factura, usuarioProfesional: UsuarioProfesional, usuarioCliente: UsuarioCliente):
        self._id = id
        self._fecha = fecha
        self._valoracion = valoracion
        self._comentario = comentario
        self._factura = factura
        self._usuarioProfesional = usuarioProfesional
        self._usuarioCliente = usuarioCliente
    
    # Getters y setters
    def getId(self) -> int:
        return self._id
    
    def setId(self, id: int):
        self._id = id
        
    def getFecha(self) -> str:
        return self._fecha
    
    def setFecha(self, fecha: str):
        self._fecha = fecha
        
    def getValoracion(self) -> float:
        return self._valoracion
    
    def setValoracion(self, valoracion: float):
        self._valoracion = valoracion
        
    def getComentario(self) -> str:
        return self._comentario
    
    def setComentario(self, comentario: str):
        self._comentario = comentario
        
    def getFactura(self) -> Factura:
        return self._factura
    
    def setFactura(self, factura: Factura):
        self._factura = factura
        
    def getUsuarioProfesional(self) -> UsuarioProfesional:
        return self._usuarioProfesional
    
    def setUsuarioProfesional(self, usuarioProfesional: UsuarioProfesional):
        self._usuarioProfesional = usuarioProfesional
        
    def getUsuarioCliente(self) -> UsuarioCliente:
        return self._usuarioCliente
    
    def setUsuarioCliente(self, usuarioCliente: UsuarioCliente):
        self._usuarioCliente = usuarioCliente
