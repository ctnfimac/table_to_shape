from django.urls import path
from .views import download_files

app_name = 'web'

urlpatterns = [
    path('', download_files, name='download_files')
]
