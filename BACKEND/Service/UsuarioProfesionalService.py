from typing import List

from entities.usuario_profesional_entity import UsuarioProfesionalEntity
from entities.contratacion_entity import ContratacionEntity


class UsuarioProfesionalService:
    def __init__(self, usuario_profesional: UsuarioProfesionalEntity):
        self.usuario_profesional = usuario_profesional
    
    def calcularValoracion(self) -> float:
        contrataciones: List[ContratacionEntity] = self.usuario_profesional.getContrataciones()
        total_valoraciones = 0
        cantidad_valoraciones = 0
        for contratacion in contrataciones:
            if contratacion.getValoracion() is not None:
                total_valoraciones += contratacion.getValoracion()
                cantidad_valoraciones += 1
        if cantidad_valoraciones == 0:
            return 0
        else:
            return total_valoraciones / cantidad_valoraciones
