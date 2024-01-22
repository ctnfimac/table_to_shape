from django.http import JsonResponse
from web.utils.database_conection import DatabaseConection

def tables_view(request, schema:str):
    tables = []
    if request.method == 'GET':
        db = DatabaseConection()
        tables = db.get_tables(schema)
    return JsonResponse({'tables': tables})

