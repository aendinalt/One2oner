from django import forms
from models import *


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record

