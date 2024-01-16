from django.conf import settings
from django.shortcuts import render
from web.forms.conectionForms import ConectionForm
from web.utils.table_to_chape_actions import build_files_geographicals, compress_directory, download_zip
from django.http import JsonResponse


def download_files(request):
    if request.method == 'POST':
        try:
            build_files_geographicals(settings.PATH_FILES)
            compress_directory(settings.PATH_DIRECTORY_CURRENT, settings.PATH_ZIP)
            return download_zip(settings.PATH_ZIP)
        except Exception as e:
            print(e.__str__())
            
    elif request.method == 'GET':
        context = {
            'conectionForm': ConectionForm()
        }
        return render(request, 'web/index.html', context)
