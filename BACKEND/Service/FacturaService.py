class FacturaService:
    def imprimirFactura(self, factura):
        print("Factura N°", factura.getNumero())
        print("Importe: $", factura.getImporte())
        print("Fecha:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
