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
                'errors': None,
                'tables':[['techos_inteligentes'], ['recorridos'], ['barrios']],
                'schemas': [['public']]
            }
        )
