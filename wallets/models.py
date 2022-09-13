import uuid

from django.db import models


class Wallet(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    asset_ticket = models.CharField(max_length=10)
    wallet_value = models.DecimalField(max_digits=50, decimal_places=15, default=0)
    crypto_quantity = models.DecimalField(max_digits=50, decimal_places=15, default=0)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="wallets"
    )
