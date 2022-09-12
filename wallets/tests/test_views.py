from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from users.models import User


class WalletViewTeste(APITestCase):
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
            ...
        }
        cls.user_login = User.objects.create_user(**cls.user)
        cls.user_login_token = Token.objects.get_or_create(user=cls.user_login)
