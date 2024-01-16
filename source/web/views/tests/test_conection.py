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
            'host': 'database',
            'dbname': 'gis',
            'port': '5432',
            'user': 'gis',
            'password': '1234'
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
                'errors': None
            }
        )

    def test_conection_with_invalid_credentials(self):
        """
        Verifico la no conexión a la base de datos con las credenciales incorrectas
        """
        response = self.client.post(self.url , self.invalid_credentials)
        self.assertEqual(response.status_code, 200)

        self.assertJSONEqual(
            response.content,
            {
                'success': True,
                'status': 200,
                'has_error': True,
                'errors': 'connection to server at "database" (172.25.0.2), port 5432 failed: FATAL:  password authentication failed for user "gis"\n'
            }
        )
