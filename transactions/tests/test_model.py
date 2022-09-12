from django.test import TestCase
from transactions.models import Transaction
from wallets.models import Wallet


class TransactionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.wallet_data = {
            "name": "testecoin",
            "asset_ticket": "TST",
        }
        cls.wallet = Wallet.objects.create(**cls.wallet_data)

        cls.transaction_data = {
            "quantity": 2.1,
            "exchange": "buy",
            "wallets": cls.wallet.id
        }
        cls.transaction = Transaction.objects.create(**cls.transaction_data, wallet=cls.wallet)

    def test_transaction_has_information_fields(self):
        self.assertEqual(self.transaction.quantity, self.transaction_data["quantity"])
        self.assertEqual(self.transaction.exchange, self.transaction_data["exchange"])
        self.assertEqual(self.transaction.wallets, self.wallet.id)
        
    def test_transaction_with_wallet_relationship_made(self):
        self.transaction.wallets = self.wallet.id
        self.transaction.save()
        self.assertIs(self.wallet.id, self.transaction.wallets)
