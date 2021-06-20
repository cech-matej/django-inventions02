import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Invention


class InventionModelForm(ModelForm):
    def clean_inventors(self):
        data = self.cleaned_data['inventors']
        if len(data) < 1:
            raise ValidationError('Neplatný počet vynálezců: musí být větší nebo roven 1')
        return data

    def clean_date(self):
        data = self.cleaned_data['date_of_invention']
        if data > datetime.datetime.now():
            raise ValidationError('Neplatné datum')
        return data

    def clean_category(self):
        data = self.cleaned_data['category']
        if len(data) < 1:
            raise ValidationError('Neplatný počet kategorií: musí být větší nebo roven 1')
        return data

    class Meta:
        model = Invention
        fields = ['name', 'inventors', 'description', 'date_of_invention', 'category', 'photo']
        labels = {'name': 'Jméno vynálezu', 'inventors': 'Jméno vynálezce', 'description': 'Popis vynálezu',
                  'date_of_invention': 'Datum vynalezení', 'category': 'Kategorie', 'photo': 'Fotografie vynálezu'}
