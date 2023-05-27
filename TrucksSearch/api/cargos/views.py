from django.db.models import Value
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.cargos.filters import CargoFilter
from api.cargos.serializers import (CargoCreateSerializer,
                                    CargoDetailSerializer, CargoListSerializer)
from cargos.models import Cargo
from config import settings
from trucks.models import Truck


class CargoViewSet(ModelViewSet):
    queryset = Cargo.objects.select_related('pick_up', 'delivery')
    filter_backends = [DjangoFilterBackend]
    filterset_class = CargoFilter
    http_method_names = ['get', 'patch', 'options', 'head', 'delete', 'post']

    def get_serializer_class(self):
        if self.action == 'create':
            self.serializer_class = CargoCreateSerializer
        elif self.action == 'list':
            self.serializer_class = CargoListSerializer
        else:
            self.serializer_class = CargoDetailSerializer
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).annotate(
            near_trucks_amount=Value(0),
        )
        if len(queryset) == 0:
            return super().list(request, *args, **kwargs)

        trucks = Truck.objects.select_related('location')
        max_distance = (
            queryset[0].max_distance
            if hasattr(queryset[0], 'max_distance')
            else settings.DEFAULT_MAX_DISTANCE
        )

        for cargo in queryset:
            near_trucks = 0
            for truck in trucks:
                if truck.location.get_distance(cargo.pick_up) <= max_distance:
                    near_trucks += 1
            cargo.near_trucks_amount = near_trucks

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
