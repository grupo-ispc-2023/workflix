class FacturaEntity:
    def __init__(self, id, numero, importe):
        self.id = id
        self.numero = numero
        self.importe = importe

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getNumero(self):
        return self.numero

    def setNumero(self, numero):
        self.numero = numero

    def getImporte(self):
        return self.importe

    def setImporte(self, importe):
        self.importe = importe
