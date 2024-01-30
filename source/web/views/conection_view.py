import psycopg2, json
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
        status = 200
        has_error = True
        schemas = []
        tables = []
        try:
            db = DatabaseConection(form.cleaned_data)
            db.test_conection_postgresql()
            schemas = db.get_schemas()
            # asigno las tablas del primer esquema retornado
            tables = db.get_tables(schemas[0][0])
            has_error = False
            msg = 'Conection ok'
        except (Exception, psycopg2.DatabaseError) as error:
            status = 500
            msg = 'Credentials incorrects'
        finally:
            return JsonResponse({
                'success': True,
                'status': status,
                'has_error': has_error,
                'errors': msg,
                'tables': tables,
                'schemas': schemas
            }, status=status)
    
    def form_invalid(self, form) -> JsonResponse:
        errors = json.loads(form.errors.as_json())
        return JsonResponse({
            'success': True,
            'status': 500,
            'has_error': True,
            'errors': list(errors.keys())
        }, status=500)

