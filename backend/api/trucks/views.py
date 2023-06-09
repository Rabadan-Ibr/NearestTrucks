from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from api.trucks.serializers import TruckListSerializer, TruckUpdateSerializer
from trucks.models import Truck


class TruckViewSet(ListModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckListSerializer
    http_method_names = ['get', 'patch', 'options', 'head']

    def get_serializer_class(self):
        if self.action == 'partial_update':
            self.serializer_class = TruckUpdateSerializer
        return super().get_serializer_class()
