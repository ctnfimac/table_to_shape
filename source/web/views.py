from django.shortcuts import render
from .actions import build_files_geographicals, compress_directory, download_zip

PATH_ZIP = '/home/gisuser/files.zip'
PATH_DIRECTORY_CURRENT = '/tmp'
# ruta en donde se guardaran los archivos .shp y asociados
PATH_FILES = PATH_DIRECTORY_CURRENT + '/'


def download_files(request):
    if request.method == 'POST':
        print('hola')
        try:
            build_files_geographicals(PATH_FILES)
            compress_directory(PATH_DIRECTORY_CURRENT, PATH_ZIP)
            #TODO:NO DESCARGA EL ZIP SINO LOS ARCHIVOS EN /tmp/
            return download_zip(PATH_ZIP)
        except Exception as e:
            print(e.__str__())
    else:
        context = {
        }
        return render(request, 'web/index.html', context)
