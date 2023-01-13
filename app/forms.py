from django.forms import ModelForm
from app.models import *
from django import forms

class TestForm(ModelForm):
    class Meta:
        model = Language
        fields = ['lang']
        widgets = {
            'lang': forms.TextInput(attrs={"class": "form-control"}),  
            
        }
    field_order = ['lang']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title_uz', 'title_ru', 'title_en', 'price', 'photo']
        labels = {
            'title_uz': 'Название (UZ)', 
            'title_ru': 'Название (RU)', 
            'title_en': 'Название (ENG)', 
            'price': 'Цена',
            'photo': 'Фото'
        }

    field_order = ['title_uz', 'title_ru', 'title_en', 'price', 'photo']
