from rest_framework import serializers

from locations.models import Location
from trucks.models import Truck


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ('id', 'location', 'payload')


class TruckUpdateSerializer(TruckSerializer):
    location = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
    )

    class Meta(TruckSerializer.Meta):
        read_only_fields = ('id', 'payload')


class TruckListSerializer(TruckSerializer):
    pass
