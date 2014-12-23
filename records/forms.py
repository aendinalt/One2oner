from django import forms
from models import *
from django.forms.models import modelformset_factory


AnswerFormSet = modelformset_factory(Answer)


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record



