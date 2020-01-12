from django.forms import ModelForm
from .models import ArtikelModel

class ArtikelForm(ModelForm):
    class Meta:
        model = ArtikelModel
        fields = ['judul','isi','penulis']

