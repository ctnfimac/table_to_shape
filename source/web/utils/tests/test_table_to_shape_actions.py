import os
from django.test import TestCase
from web.utils.database_conection import DatabaseConection
from source.web.utils.table_to_shape_actions import build_files_geographicals, compress_directory

class TableToShapeTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.credentials = {
            'host': 'database',
            'dbname': 'gis',
            'port': '5432',
            'user': 'gis',
            'password': 'gis123'
        }

        cls.conection = DatabaseConection(cls.credentials)
    

    def test_build_files_geographicals(self):
        '''
        Verifico si se generan los 15 archivos geograficos de las 3 tablas seleccionadas
        '''
        build_files_geographicals('/tmp/','public',['barrios','recorridos','techos_inteligentes'])
        files_len = len(os.listdir('/tmp/'))
        
        self.assertEqual(files_len, 15)


    def test_compress_directory(self):
        '''
        Verifico si se generó en .zip
        '''
        compress_directory('/tmp','/home/gisuser/files.zip')
        self.assertTrue(os.path.isfile('/home/gisuser/files.zip'))
