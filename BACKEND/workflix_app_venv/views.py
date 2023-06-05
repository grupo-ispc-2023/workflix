from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ServicioSerializer
from .serializer import ProvinciaSerializer
from .serializer import CiudadSerializer
from .models import Servicio
from .models import Provincia
from .models import Ciudad


# Create your views here.

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
