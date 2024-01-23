import psycopg2
from django.urls import reverse_lazy
from web.forms.conectionForms import ConectionForm
from django.views.generic import FormView
from django.http import JsonResponse
from web.utils.database_conection import DatabaseConection

class ConectionView(FormView):
    form_class = ConectionForm
    template_name = reverse_lazy('web:download_files')
    success_url = reverse_lazy('web:download_files')
    
    def form_valid(self, form) -> JsonResponse:
        has_error = True
        response_error = None
        schemas = []
        tables = []
        try:
            db = DatabaseConection(form.cleaned_data)
            db.test_conection_postgresql()
            schemas = db.get_schemas()
            # asigno las tablas del primer esquema retornado
            tables = db.get_tables(schemas[0][0])
            has_error = False
        except (Exception, psycopg2.DatabaseError) as error:
            print(f'Error {error}')
            response_error = error.__str__()
        finally:
            return JsonResponse({
                'success': True,
                'status': 200,
                'has_error': has_error,
                'errors': response_error,
                'tables': tables,
                'schemas': schemas
            })
    
    def form_invalid(self, form) -> JsonResponse:
        errors = form.errors
        return JsonResponse({
            'success': True,
            'status': 400,
            'has_error': True,
            'errors': errors
        })

