    @abstractmethod
    def crearUsuario(self):
        pass

    @abstractmethod
    def borrarUsuario(self):
        pass

    @abstractmethod
    def ModificarDatos(self, usuario):
        pass

    @abstractmethod
    def elegirRol(self):
        pass

    @abstractmethod
    def elegirProvincia(self, provincia):
        pass

    @abstractmethod
    def elegirCiudad(self, ciudad):
        pass

    @abstractmethod
    def cargarFotoPerfil(self):
        pass