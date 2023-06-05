from rest_framework import viewsets, permissions
from .models import Servicio
from .models import Provincia
from .models import Ciudad
from .serializer import ServicioSerializer
from .serializer import ProvinciaSerializer
from .serializer import CiudadSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ServicioSerializer

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProvinciaSerializer

class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CiudadSerializer