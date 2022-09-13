from django.test import TestCase
from users.models import User
from wallets.models import Wallet


class WalletModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = {
            "username": "testando",
            "email": "teste@mail.com",
            "password": "1234",
            "birth_date": "1990-01-01",
            "first_name": "Testador",
            "last_name": "da Silva",
            "cpf": "856.135.217-51",
        }
        cls.person = User.objects.create_user(**cls.user)

        cls.wallet = {
            "name": "testecoin",
            "asset_ticket": "TST",
        }
        cls.my_wallet = Wallet.objects.create(**cls.wallet, user=cls.person)

    def test_wallet_has_information_fields(self):
        self.assertEqual(self.my_wallet.name, self.wallet["name"])
        self.assertEqual(self.my_wallet.asset_ticket, self.wallet["asset_ticket"])
        self.assertEqual(self.my_wallet.person, self.person)
        
    def test_wallet_with_user_relationship_made(self):
        self.my_wallet.user_id = self.person.id
        self.my_wallet.save()
        self.assertIs(self.person.id, self.my_wallet.user_id)
