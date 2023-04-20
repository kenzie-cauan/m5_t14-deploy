from rest_framework import serializers
from .models import Account, ShiftOptions


class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    shift = serializers.ChoiceField(
        choices=ShiftOptions.choices,
        default=ShiftOptions.DEFAULT,
    )
    first_name = serializers.CharField(max_length=127)
    last_name = serializers.CharField(max_length=127)

    email = serializers.EmailField(max_length=127)
    username = serializers.CharField(max_length=150)

    password = serializers.CharField(max_length=128, write_only=True)

    def create(self, validated_data: dict) -> Account:
        return Account.objects.create_user(**validated_data)

    def update(self, instance: Account, validated_data: dict) -> Account:
        """
        Falta implementar a parte de hashear o password, caso seha passado.
        """
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
