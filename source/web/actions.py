import os
import psycopg2
import zipfile
import geopandas as gpd
from django.http.response import HttpResponse
from decouple import config


def armar_archivos_shape(ruta_directorio:str='./badata/tmp/') -> None:
    credenciales_db = {
        "host": config('EXTERNAL_DATABASE_HOST'),
        "dbname": config('EXTERNAL_DATABASE_NAME'),
        "port": config('EXTERNAL_DATABASE_PORT'),
        "user": config('EXTERNAL_DATABASE_USER'),
        "password": config('EXTERNAL_DATABASE_PASSWORD')
    }
    #TODO:poner tablas
    tablas = ['calles_dataset_badata']
    conn = psycopg2.connect(**credenciales_db)
    
    for tabla in tablas:
        sql_query = f'SELECT * FROM auto_badata.{tabla}'
        gdf = gpd.read_postgis(sql_query, con=conn)
        # Guarda el GeoDataFrame como un Shapefile
        path = f'{ruta_directorio}{tabla}.shp'
        gdf.to_file(path, driver='ESRI Shapefile')


def comprimir_directorio(ruta_directorio:str, ruta_zip:str) -> None:
    with zipfile.ZipFile(ruta_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for carpeta_actual, _, archivos in os.walk(ruta_directorio):
            for archivo in archivos:
                ruta_completa = os.path.join(carpeta_actual, archivo)
                ruta_relativa = os.path.relpath(ruta_completa, ruta_directorio)
                zipf.write(ruta_completa, arcname=ruta_relativa)


def descargar_zip(ruta_zip: str):
    if os.path.exists(ruta_zip):
        with open(ruta_zip, 'rb') as archivo_zip:
            response = HttpResponse(archivo_zip.read(), content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename= badata.zip' 
            return response
    else:
        print('no existe')
