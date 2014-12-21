from django import forms
from models import *


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        widgets = {
            'questions': forms.CheckboxSelectMultiple()
        }

