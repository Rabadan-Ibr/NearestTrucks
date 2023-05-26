from rest_framework import serializers

from TrucksSearch import settings
from cargos.models import Cargo
from locations.models import Location


class CargoCreateSerializer(serializers.ModelSerializer):
    pick_up = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all()
    )
    delivery = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all()
    )

    class Meta:
        model = Cargo
        fields = ('pick_up', 'delivery', 'weight', 'description')


class CargoListSerializer(serializers.ModelSerializer):
    pick_up = serializers.StringRelatedField()
    delivery = serializers.StringRelatedField()
    near_trucks_count = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = ('id', 'pick_up', 'delivery', 'near_trucks_count')

    def get_near_trucks_count(self, cargo):
        """
        Return: The number of trucks located no more than a specified distance.
        """
        count = 0
        max_distance = (
            cargo.max_distance
            if hasattr(cargo, 'max_distance')
            else settings.DEFAULT_MAX_DISTANCE
        )
        for truck in cargo.trucks:
            if truck['distance'] <= max_distance:
                count += 1
        return count


class TruckInCargoSerializer(serializers.Serializer):
    truck_id = serializers.CharField()
    distance = serializers.IntegerField()


class CargoDetailSerializer(serializers.ModelSerializer):
    pick_up = serializers.StringRelatedField()
    delivery = serializers.StringRelatedField()
    trucks = TruckInCargoSerializer(many=True, read_only=True)

    class Meta:
        model = Cargo
        fields = (
            'id', 'pick_up', 'delivery', 'weight', 'description', 'trucks'
        )
        read_only_fields = ('id', 'pick_up', 'delivery')
