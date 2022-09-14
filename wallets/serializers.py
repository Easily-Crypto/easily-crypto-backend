from rest_framework import serializers
from transactions.api_data import DataCrypto
from transactions.serializers import TransactionsSerializer

from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    transactions = TransactionsSerializer(many=True, read_only=True)

    class Meta:
        model = Wallet
        fields = "__all__"
        read_only_fields = ["user"]

    def create(self, validated_data):
        data = DataCrypto.get(crypto=validated_data["asset_ticket"])
        if data:
            wallet = Wallet.objects.create(**validated_data)
            return wallet
        else:
           raise serializers.ValidationError({"error":f"The {validated_data['asset_ticket']} not exist in API database."})
