import json
from django.test import TestCase
from django.urls import reverse


class ConectionTest(TestCase):

    url = reverse('web:conection')

    @classmethod
    def setUpTestData(cls) -> None:
        cls.valid_credentials = {
            'host': 'database',
            'dbname': 'gis',
            'port': '5432',
            'user': 'gis',
            'password': 'gis123'
        }

        cls.invalid_credentials = {
            'host': '127.0.0.1',
            'dbname': 'gis',
            'port': '5432',
            'user': 'pok',
            'password': '123'
        }

        cls.incomplete_credentials = {
            'dbname': 'gis',
            'port': '5432',
            'password': 'gis123'
        }


    def test_conection_with_valid_credentials(self):
        """
        Verifico la conexión a la base de datos con las credenciales correctas
        """
        response = self.client.post(self.url , self.valid_credentials)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            {
                'success': True,
                'status': 200,
                'has_error': False,
                'errors': 'Conection ok',
                'tables':[['techos_inteligentes'], ['recorridos'], ['barrios']],
                'schemas': [['public']]
            }
        )

    
    def test_conection_with_invalid_credentials(self):
        """
        Verifico la no conexión a la base de datos con las credenciales incorrectas
        """
        response = self.client.post(self.url , self.invalid_credentials)
        self.assertEqual(response.status_code, 500)

        self.assertJSONEqual(
            response.content,
            {
                'success': True,
                'status': 500,
                'has_error': True,
                'errors': 'Credentials incorrects',
                'tables': [],
                'schemas': []
            }
        )


    def test_conection_with_incomplete_credentials(self):
        """
        Verifico error cuando falta el dato de unos de los campos en el 
        formulario
        """
        response = self.client.post(self.url , self.incomplete_credentials)
        self.assertEqual(response.status_code, 500)

        self.assertJSONEqual(
            response.content,
            {
                'success': True,
                'status': 500,
                'has_error': True,
                'errors': ['host', 'user'],
            }
        )

