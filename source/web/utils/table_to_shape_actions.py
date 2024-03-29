import os, zipfile, geopandas as gpd
from sqlalchemy import create_engine  
from django.http.response import HttpResponse
from web.utils.database_conection import DatabaseConection


def build_files_geographicals(path_directory:str='/tmp/', schema:str='public', tables:list=[]) -> None:
    db = DatabaseConection()
    con = create_engine(db.credentials_sqlalchemy())  

    #elimino los archivos geográficos actuales en el directorio
    os.system('rm /tmp/*')

    for table in tables:
        sql_query = f'SELECT * FROM {schema}.{table}'
        df = gpd.read_postgis(sql_query, con=con)
        # Guarda el GeoDataFrame como un Shapefile
        path = f'{path_directory}{table}.shp'
        df.to_file(path, driver='ESRI Shapefile')

    con.dispose()


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
