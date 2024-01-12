import psycopg2
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import FormView
from .actions import build_files_geographicals, compress_directory, download_zip
from .forms.conectionForms import ConectionForm

PATH_ZIP = '/home/gisuser/files.zip'
PATH_DIRECTORY_CURRENT = '/tmp'
# ruta en donde se guardaran los archivos .shp y asociados
PATH_FILES = PATH_DIRECTORY_CURRENT + '/'


def download_files(request):
    if request.method == 'POST':
        try:
            build_files_geographicals(PATH_FILES)
            compress_directory(PATH_DIRECTORY_CURRENT, PATH_ZIP)
            return download_zip(PATH_ZIP)
        except Exception as e:
            print(e.__str__())
    else:
        context = {
            'conectionForm': ConectionForm()
        }
        return render(request, 'web/index.html', context)

#TODO: utilizar patron singleton para la conexión
class ConectionView(FormView):
    form_class = ConectionForm
    template_name = reverse_lazy('web:download_files')
    success_url = reverse_lazy('web:download_files')
    def form_valid(self, form) -> JsonResponse:
        conn = None
        has_error = True
        response_error = None
        try:
            credenciales_db = {
                "host": form.cleaned_data['host'],
                "dbname": form.cleaned_data['dbname'],
                "port": form.cleaned_data['port'],
                "user": form.cleaned_data['user'],
                "password": form.cleaned_data['password'] 
            }
            conn = psycopg2.connect(**credenciales_db)
            has_error = False
        except (Exception, psycopg2.DatabaseError) as error:
            print(f'Error {error}')
            response_error = error.__str__()
        finally:
            return JsonResponse({
                'success': True,
                'status': 200,
                'has_error': has_error,
                'errors': response_error
            })
    
    def form_invalid(self, form) -> JsonResponse:
        errors = form.errors
        return JsonResponse({
            'success': True,
            'status': 400,
            'has_error': True,
            'errors': errors
        })

