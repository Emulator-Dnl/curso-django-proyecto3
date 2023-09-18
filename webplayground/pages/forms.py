from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        # Con widgets podemos definir la clase del campo para que se muestre el estilo
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control'}),
        }
        # Normalmente toma lo definido en el modelo, pero también se puede definir aquí
        labels = {
            'title':'Título', 'order':'Orden', 'content': 'Contenido'
        }