from rest_framework import serializers
from transactions.api_data import DataCrypto
from transactions.models import Transaction
from transactions.serializers import TransactionsSerializer
from django.shortcuts import get_object_or_404, get_list_or_404

from users.serializers import UserSerializer
from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    transactions = TransactionsSerializer(many=True, read_only=True)
    sub_total = serializers.SerializerMethodField()

    class Meta:
        model = Wallet
        fields = "__all__"
        read_only_fields = ["user"]

    def get_sub_total(self, obj):

        wallet = get_object_or_404(Wallet, pk=obj.pk)
        transactions = Transaction.objects.filter(wallets=obj.pk)

        quantity = sum([float(item.quantity) for item in transactions])

        crypto_quotation = float(
            DataCrypto.get(crypto=wallet.asset_ticket)["price_actual"]
        )
        data = {"value": quantity * crypto_quotation}
        return data["value"]

    def create(self, validated_data):
        wallet = Wallet.objects.create(**validated_data)

        return wallet

    # def update(self, instance, validated_data):

    #     print(instance.sub_total)
    #     print(validated_data)
    #     instance.sub_total = validated_data

    #     # instance.is_valid(raise_exception=True)
    #     # instance.save()

    #     return instance
