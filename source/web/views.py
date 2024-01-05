from django.shortcuts import render
from .actions import armar_archivos_shape, descargar_zip, comprimir_directorio

# Create your views here.
#TODO:Estas rutas modificarlas para que no influya dentro del proyecto
# ruta y nombre del archivo .zip que se generará
RUTA_ZIP = './badata/badata.zip'
RUTA_DIRECTORIO_TEMPORAL = './badata/tmp'
# ruta en donde se guardaran los archivos .shp y asociados
RUTA_ARCHIVOS = RUTA_DIRECTORIO_TEMPORAL + '/'


def download_files(request):
    if request.method == 'POST':
        try:
            armar_archivos_shape(RUTA_ARCHIVOS)
            comprimir_directorio(RUTA_DIRECTORIO_TEMPORAL, RUTA_ZIP)
            return descargar_zip(RUTA_ZIP)
        except Exception as e:
            print(e.__str__())
    else:
        context = {
        }
        return render(request, 'web/index.html', context)
