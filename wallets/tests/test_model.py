from django.test import TestCase
from users.models import User
from wallets.models import Wallet


class WalletModelTest(TestCase):
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

    def test_wallet_has_information_fields(self):
        self.assertEqual(self.wallet.name, self.wallet_data["name"])
        self.assertEqual(self.wallet.asset_ticket, self.wallet_data["asset_ticket"])
        self.assertEqual(self.wallet.user, self.user)
        
    def test_wallet_with_user_relationship_made(self):
        self.wallet.user_id = self.user.id
        self.wallet.save()
        self.assertIs(self.user.id, self.wallet.user_id)
