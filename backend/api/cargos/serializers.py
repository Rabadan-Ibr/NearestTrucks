from rest_framework import serializers

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
    near_trucks_amount = serializers.IntegerField(read_only=True)

    class Meta:
        model = Cargo
        fields = ('id', 'pick_up', 'delivery', 'near_trucks_amount')


class TruckInCargoSerializer(serializers.Serializer):
    truck_id = serializers.CharField()
    distance = serializers.IntegerField()


class CargoDetailUpdateSerializer(serializers.ModelSerializer):
    pick_up = serializers.StringRelatedField()
    delivery = serializers.StringRelatedField()
    trucks = TruckInCargoSerializer(many=True, read_only=True)

    class Meta:
        model = Cargo
        fields = (
            'id', 'pick_up', 'delivery', 'weight', 'description', 'trucks'
        )
        read_only_fields = ('id', 'pick_up', 'delivery')
