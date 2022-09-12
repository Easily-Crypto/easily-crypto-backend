from rest_framework import serializers
from transactions.serializers import TransactionsSerializer

from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    transactions = TransactionsSerializer(many=True, read_only=True)

    class Meta:
        model = Wallet
        fields = "__all__"
        read_only_fields = ["user"]

    def create(self, validated_data):
        wallet = Wallet.objects.create(**validated_data)

        return wallet

    def update(self, instance, validated_data):

        print(instance.sub_total)
        print(validated_data)
        instance.sub_total = validated_data

        # instance.is_valid(raise_exception=True)
        # instance.save()

        return instance
