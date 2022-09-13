from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Request, Response, status
from transactions.api_data import DataCrypto

from wallets.models import Wallet
from wallets.serializers import WalletSerializer

from .permissions import IsOwnerWallet


class WalletView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()

    lookup_url_kwarg = "wallet_id"

    def perform_create(self, serializer):

        crypto_is_valid = DataCrypto.get(crypto=self.request.data["asset_ticket"])

        serializer.save(user=self.request.user)


class SubTotalWalletView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerWallet]

    def get(self, req: Request, wallet_id) -> Response:

        wallet = get_object_or_404(Wallet, pk=wallet_id)
        serialized = WalletSerializer(wallet)
        self.check_object_permissions(req, obj=serialized.data)

        quantity = sum(
            [
                float(item["quantity"])
                if item["exchange"] == "buy"
                else -float(item["quantity"])
                for item in serialized.data["transactions"]
            ]
        )

        crypto_quotation = float(
            DataCrypto.get(crypto=wallet.asset_ticket)["price_actual"]
        )

        data = {"sub_total": quantity * crypto_quotation}

        sub_total_serialized = WalletSerializer(wallet, data=data, partial=True)

        sub_total_serialized.is_valid(raise_exception=True)

        sub_total_serialized.save()

        return Response(sub_total_serialized.data, status.HTTP_200_OK)
