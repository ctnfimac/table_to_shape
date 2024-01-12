from django.urls import path
from .views import download_files, ConectionView

app_name = 'web'

urlpatterns = [
    path('', download_files, name='download_files'),
    path('conection', ConectionView.as_view(), name='conection')
]
