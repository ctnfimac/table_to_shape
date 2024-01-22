from django.urls import path
from web.views.download_files_view import download_files
from web.views.conection_view import ConectionView
from web.views.tables_view import tables_view

app_name = 'web'

urlpatterns = [
    path('', download_files, name='download_files'),
    path('conection', ConectionView.as_view(), name='conection'),
    path('tables/<str:schema>', tables_view, name='tables')
]
