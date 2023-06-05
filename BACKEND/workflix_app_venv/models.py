from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=50, blank=False, default='')
    descripcion = models.CharField(max_length=100, blank=False, default='')

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length=100, blank=False)

    def _str_(self):
        return self.nombre_provincia

class Ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_ciudad = models.CharField(max_length=100, blank=False)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def _str_(self):
        return self.nombre_ciudad

class Profesion(models.Model):
    id_Profesion = models.AutoField(primary_key=True)
    nombre_Profesion = models.CharField(max_length=100, blank=False)
    descripcion = models.TextField(max_length=500, blank=False)

    def __str__(self):
        return self.nombre_Profesion

    
