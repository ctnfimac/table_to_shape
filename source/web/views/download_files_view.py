from django.conf import settings
from django.shortcuts import render
from web.forms.conectionForms import ConectionForm
from web.utils.table_to_shape_actions import build_files_geographicals, compress_directory, download_zip


def download_files(request):
    if request.method == 'POST':
        try:
            schema = request.POST.get('schema','public')
            tables = request.POST.getlist('tablesdb','')
            build_files_geographicals(settings.PATH_FILES, schema, tables)
            compress_directory(settings.PATH_DIRECTORY_CURRENT, settings.PATH_ZIP)
            return download_zip(settings.PATH_ZIP)
        except Exception as e:
            print(e.__str__())
            
    elif request.method == 'GET':
        context = {
            'conectionForm': ConectionForm()
        }
        return render(request, 'web/index.html', context)
