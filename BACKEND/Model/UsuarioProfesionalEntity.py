class UsuarioProfesionalEntity(Usuario):
    def __init__(self, id: int, nombre: str, apellido: str, email: str, contrasena: str,
                 telefono: str, fotoPerfil: str, rol: Rol, provincia: Provincia, ciudad: Ciudad,
                 descripcion: str, calificacionObtenida: float, servicios: List[Servicio]):
        super().__init__(id, nombre, apellido, email, contrasena, telefono, fotoPerfil, rol, provincia, ciudad)
        self.descripcion = descripcion
        self.calificacionObtenida = calificacionObtenida
        self.servicios = servicios

    def getDescripcion(self) -> str:
        return self.descripcion

    def setDescripcion(self, descripcion: str) -> None:
        self.descripcion = descripcion

    def getCalificacionObtenida(self) -> float:
        return self.calificacionObtenida

    def setCalificacionObtenida(self, calificacionObtenida: float) -> None:
        self.calificacionObtenida = calificacionObtenida

    def getServicios(self) -> List[Servicio]:
        return self.servicios

    def setServicios(self, servicios: List[Servicio]) -> None:
        self.servicios = servicios
