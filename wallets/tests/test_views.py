from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from users.models import User
from wallets.models import Wallet


class WalletViewTest(APITestCase):
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
        cls.wallet = {
            "name": "testecoin",
            "asset_ticket": "TST",
        }
        cls.person = User.objects.create_user(**cls.user)
        cls.person_token = Token.objects.get_or_create(user=cls.person)

    def test_create_wallet(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.person_token[0]}")
        response = self.client.post("/api/wallets/", self.wallet, format="json")
        self.assertEqual(201, response.status_code)

    def test_create_wallet_without_user(self):
        response = self.client.post("/api/wallets/", self.wallet, format="json")
        self.assertEqual(401, response.status_code)
        self.assertIn("detail", response.data)
