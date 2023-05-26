from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.cargos.views import CargoViewSet
from api.trucks.views import TruckViewSet

app_name = 'api'

v1_router = DefaultRouter()
v1_router.register('cargo', CargoViewSet, basename='cargo')
v1_router.register('truck', TruckViewSet, basename='truck')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
