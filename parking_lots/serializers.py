from rest_framework import serializers

from accounts.serializers import AccountSerializer
from .models import ParkingLot


class ParkingLotSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)

    class Meta:
        model = ParkingLot
        fields = ["id", "name", "account"]
        # depth = 2
        # fields = "__all__"
