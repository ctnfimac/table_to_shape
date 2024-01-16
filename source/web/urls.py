from django.urls import path
from web.views.download_files_view import download_files
from web.views.conection_view import ConectionView

app_name = 'web'

urlpatterns = [
    path('', download_files, name='download_files'),
    path('conection', ConectionView.as_view(), name='conection')
]
