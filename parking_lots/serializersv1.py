from rest_framework import serializers
from .models import ParkingLot


class ParkingLotSerializerV1(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    def create(self, validated_data: dict) -> ParkingLot:
        return ParkingLot.objects.create(**validated_data)

    def update(self, instance: ParkingLot, validated_data: dict) -> ParkingLot:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
