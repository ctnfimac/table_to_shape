from django import forms

class ConectionForm(forms.Form):
    host = forms.CharField(
        label='Servidor', 
        max_length=15,
        initial='database',
        widget=forms.TextInput(
            attrs={
                'class':'form-control mb-2',
                'placeholder': 'Ingrese la Ip del Servidor'
            }
        )    
    )
    dbname = forms.CharField(
        label='Base de Datos', 
        max_length=15,
        initial='gis',
        widget=forms.TextInput(
            attrs={
                'class':'form-control mb-2',
                'placeholder': 'Ingrese Nombre de la Base de datos'
            }
        )  
    )
    port = forms.CharField(
        label='Puerto', 
        max_length=4,
        initial='5432',
        widget=forms.TextInput(
            attrs={
                'class':'form-control mb-2',
                'placeholder': 'Ingrese el Puerto'
            }
        )
    )
    user = forms.CharField(
        label='Usuario', 
        max_length=15,
        initial='gis',
        widget=forms.TextInput(
            attrs={
                'class':'form-control mb-2',
                'placeholder': 'Ingrese el Usuario'
            }
        )
    )
    password = forms.CharField(
        label='Contraseña', 
        max_length=50,
        initial='gis123',
        widget=forms.TextInput(
            attrs={
                'class':'form-control mb-2',
                'placeholder': 'Ingrese la Contraseña'
            }
        )
    )


    class Media:
        js = ('js/conectionForm.js',)
