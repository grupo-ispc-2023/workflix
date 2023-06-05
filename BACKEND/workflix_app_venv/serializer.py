from rest_framework import serializers
from .models import Servicio
from .models import Provincia
from .models import Ciudad

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ('id',
                'nombre',
                'descripcion')

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ('id',
                'nombre_provincia')

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('id',
                'nombre_ciudad',
                'provincia')
        