from django.test import TestCase
from django.urls import reverse, reverse_lazy
from web.utils.database_conection import DatabaseConection

class DatabaseConectionTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.credentials = {
            'host': '127.0.0.1',
            'dbname': 'gis',
            'port': '5432',
            'user': 'gis44',
            'password': 'gis123'
        }

        cls.credentials_new = {
            'host': 'database',
            'dbname': 'gis',
            'port': '5432',
            'user': 'gis',
            'password': 'gis123'
        }

        cls.conection = DatabaseConection(cls.credentials)
    

    def test_create_instance(self):
        '''
        Verifico si se creo la instancia con las credenciales seteadas
        '''
        self.assertIsNotNone(self.conection)
        self.assertEqual(self.conection._instance.host, '127.0.0.1')
        self.assertEqual(self.conection._instance.database, 'gis')
        self.assertEqual(self.conection._instance.port, '5432')
        self.assertEqual(self.conection._instance.user, 'gis44')
        self.assertEqual(self.conection._instance.password, 'gis123')



    def test_edit_instance(self):
        '''
        Verifico si modifico los valores de la instancia de la clase
        '''
        conection = DatabaseConection(self.credentials_new)

        self.assertIsNotNone(conection)
        self.assertEqual(self.conection._instance.host, 'database')
        self.assertEqual(self.conection._instance.database, 'gis')
        self.assertEqual(self.conection._instance.port, '5432')
        self.assertEqual(self.conection._instance.user, 'gis')
        self.assertEqual(self.conection._instance.password, 'gis123')
 


    def test_get_schemas(self):
        '''
        Este test puede variar si se agregan esquemas a la base de datos
        de prueba, originalmente solo esta public
        '''
        schemas = self.conection.get_schemas()

        self.assertEqual(len(schemas), 1)
        self.assertEqual(schemas[0][0], 'public')


    def test_get_tables(self):
        '''
        Este test puede variar si se agregan tablas al esquema public,
        originalmente hay 3
        '''
        tables = self.conection.get_tables('public')
        self.assertEqual(len(tables), 4)
        self.assertEqual(tables[0], ('techos_inteligentes',))
        self.assertEqual(tables[1], ('recorridos',))
        self.assertEqual(tables[2], ('barrios',))
