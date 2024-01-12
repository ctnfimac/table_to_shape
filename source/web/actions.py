import os, psycopg2, zipfile
from geopandas import GeoDataFrame
import geopandas as gpd
import fiona
from decouple import config
from sqlalchemy import create_engine  
from django.http.response import HttpResponse


def build_files_geographicals(path_directory:str='/tmp/') -> None:

    tables = ['techos_inteligentes','barrios','recorridos']
    db_connection_url = f"postgresql://{config('EXTERNAL_DATABASE_USER')}:{config('EXTERNAL_DATABASE_PASSWORD')}@database:{config('EXTERNAL_DATABASE_PORT')}/{config('EXTERNAL_DATABASE_NAME')}"
    con = create_engine(db_connection_url)  

    for table in tables:
        sql_query = f'SELECT * FROM public.{table}'
        df = gpd.read_postgis(sql_query, con=con)
        # Guarda el GeoDataFrame como un Shapefile
        path = f'{path_directory}{table}.shp'
        df.to_file(path, driver='ESRI Shapefile')


def compress_directory(path_directory:str, path_zip:str) -> None:
    with zipfile.ZipFile(path_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for directory_current, _, files in os.walk(path_directory):
            for file_ in files:
                path_complete = os.path.join(directory_current, file_)
                path_relative = os.path.relpath(path_complete, path_directory)
                zipf.write(path_complete, arcname=path_relative)


def download_zip(path_zip: str):
    if os.path.exists(path_zip):
        with open(path_zip, 'rb') as file_zip:
            response = HttpResponse(file_zip.read(), content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename= files.zip' 
            return response
    else:
        print('no exists')
