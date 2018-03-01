from django import forms
from django.forms import ModelForm

from models import SvtPeriod

class PeriodForm(ModelForm):
    class Meta:
        model = SvtPeriod
        fields = '__all__'
        labels = {

        }