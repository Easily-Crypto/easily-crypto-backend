from address.models import Address
from django.test import TestCase
from users.models import User


class AddressModelTest(TestCase):
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

        cls.address_data = {
            "zip_code": "80060100",
            "address": "Rua 1",
            "number": 2,
            "district": "Bairro",
            "city": "Cidade",
            "state": "Estado",
            "country": "Brasil"
        }
        cls.address = Address.objects.create(**cls.address_data, user=cls.user)

    def test_address_has_information_fields(self):
        self.assertEqual(self.address.zip_code, self.address_data["zip_code"])
        self.assertEqual(self.address.address, self.address_data["address"])
        self.assertEqual(self.address.number, self.address_data["number"])
        self.assertEqual(self.address.district, self.address_data["district"])
        self.assertEqual(self.address.city, self.address_data["city"])
        self.assertEqual(self.address.state, self.address_data["state"])
        self.assertEqual(self.address.country, self.address_data["country"])
        self.assertEqual(self.address.user.id, self.user.id)
        
    def test_address_with_wallet_relationship_made(self):
        self.address.user = self.user
        self.address.save()
        self.assertIs(self.user.id, self.address.user.id)
