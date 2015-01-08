from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    summary = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000, widget=forms.Textarea)

    def send_email(self):
        form_data = self.cleaned_data
        print form_data
        send_mail(str(form_data['summary']), str(form_data['description']),
                  'one2oner@altexsoft.com', ['andrey.matukhno@altexsoft.com'])