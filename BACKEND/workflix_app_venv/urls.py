#from django.urls import path, include
#from rest_framework import routers
#from workflix_app_venv import views

#router = routers.DefaultRouter()
#router.register(r'servicios',views.ServicioViewSet)
#urlpatterns = [
#    path('', include(router.urls)),
#]

from rest_framework import routers
from .api import ServicioViewSet
from .api import ProvinciaViewSet
from .api import CiudadViewSet

router = routers.DefaultRouter()
router.register('api/servicios', ServicioViewSet, 'servicios')
router.register('api/provincias', ProvinciaViewSet, 'provincias')
router.register('api/ciudades', CiudadViewSet, 'ciudades') 

urlpatterns = router.urls
