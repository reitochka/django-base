from django import forms
from . import models
from django.forms import ModelForm
from django.forms import widgets
import datetime

'''
class RequestForm(forms.Form):
    def __init__(self, user_id, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        a = models.Script.objects.filter(owner_id=user_id)
        SCR = [['', '']]
        for item in a.all():
            # print(item)
            SCR.append([item.name, item.name])
        self.fields['script'] = forms.ChoiceField(choices=SCR, required=False, initial='', widget=forms.Select(attrs={'class': 'form-control'}))

        self.fields['date_to'] = forms.CharField(initial=datetime.date.today(),
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))

    key = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ключ'}))
    YEARS = range(1900, 2018)
    date_from = forms.CharField(initial=datetime.date(1900, 1, 1), widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
    STATUS = [
        ['', ''],
        ['NEW', 'NEW'],
        ['TRIAL', 'TRIAL'],
        ['ACTIVE', 'ACTIVE'],
        ['EXPIRED', 'EXPIRED'],
        ['UNKNOWN', 'UNKNOWN'],
    ]
    status = forms.ChoiceField(choices=STATUS, required=False, initial='', widget=forms.Select(attrs={'class': 'form-control'}))
    
    '''