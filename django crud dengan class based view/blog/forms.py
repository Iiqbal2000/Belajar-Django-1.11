from django.forms import ModelForm
from django import forms
from .models import PostModels

class PostForms(ModelForm):
    class Meta:
        model = PostModels
        fields = [
            'judul',
            'body',
            'penulis',
            'kategori',
        ]
        widgets = {
            'judul':forms.TextInput(
                attrs = {
                    'class':'form-control',
                }
            ),

            'body':forms.Textarea(
                attrs = {
                    'class':'form-control',
                }
            ),

            'penulis':forms.TextInput(
                attrs = {
                    'class':'form-control',
                }
            ),

            'kategori':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )
        }