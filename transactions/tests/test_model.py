from django.test import TestCase
from transactions.models import Transaction
from users.models import User
from wallets.models import Wallet


class TransactionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {
            "username": "testando",
            "email": "teste@mail.com",
            "password": "1234",
            "birth_date": "1990-01-01",
            "first_name": "Testador",
            "last_name": "da Silva",
            "cpf": "856.135.217-51",
        }
        cls.user = User.objects.create_user(**cls.user_data)

        cls.wallet_data = {
            "name": "testecoin",
            "asset_ticket": "BTC",
        }
        cls.wallet = Wallet.objects.create(**cls.wallet_data, user=cls.user)

        cls.transaction_data = {
            "quantity": 2.1,
            "exchange": "buy",
            "quotation": 0.0,
            "total_value": 0
        }
        cls.transaction = Transaction.objects.create(**cls.transaction_data, wallets=cls.wallet)

    def test_transaction_has_information_fields(self):
        self.assertEqual(self.transaction.quantity, self.transaction_data["quantity"])
        self.assertEqual(self.transaction.exchange, self.transaction_data["exchange"])
        self.assertEqual(self.transaction.quotation, self.transaction_data["quotation"])
        self.assertEqual(self.transaction.total_value, self.transaction_data["total_value"])
        self.assertEqual(self.transaction.wallets.id, self.wallet.id)
        
    def test_transaction_with_wallet_relationship_made(self):
        self.transaction.wallets = self.wallet
        self.transaction.save()
        self.assertIs(self.wallet.id, self.transaction.wallets.id)
