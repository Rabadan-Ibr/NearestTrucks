from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from api.cargos.filters import CargoFilter
from api.cargos.serializers import (CargoCreateSerializer,
                                    CargoDetailSerializer, CargoListSerializer)
from cargos.models import Cargo


class CargoViewSet(ModelViewSet):
    queryset = Cargo.objects
    filter_backends = [DjangoFilterBackend]
    filterset_class = CargoFilter

    def get_serializer_class(self):
        if self.action == 'create':
            self.serializer_class = CargoCreateSerializer
        elif self.action == 'list':
            self.serializer_class = CargoListSerializer
        else:
            self.serializer_class = CargoDetailSerializer
        return super().get_serializer_class()
