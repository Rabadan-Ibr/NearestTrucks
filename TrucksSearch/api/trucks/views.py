from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from api.trucks.serializers import TruckUpdateSerializer
from trucks.models import Truck


class TruckViewSet(ListModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckUpdateSerializer

    def get_serializer_class(self):
        if self.action == 'update':
            return TruckUpdateSerializer
        return super().get_serializer_class()
