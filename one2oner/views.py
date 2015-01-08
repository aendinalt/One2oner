from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from forms import *


class DashboardView(TemplateView):
    template_name = 'dashboard.html'


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)


class ThanksView(TemplateView):
    template_name = 'thanks.html'