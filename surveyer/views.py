from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from models import *
from surveyer.forms import *


# Create your views here.


class SurveysList(ListView):
    model = Survey
    template_name = 'surveyer/list.html'


class SurveyDetail(DetailView):
    model = Survey
    template_name = 'surveyer/item.html'

    def get_context_data(self, **kwargs):
        context = super(SurveyDetail, self).get_context_data(**kwargs)
        obj = kwargs['object']
        context['questions'] = Question.objects.filter(survey__id=obj.id)
        return context


class SurveyUpdate(UpdateView):
    model = Survey
    form_class = SurveyForm
    template_name = 'surveyer/edit.html'

    def get_context_data(self, **kwargs):
        context = super(SurveyUpdate, self).get_context_data(**kwargs)
        print kwargs
        context['title'] = 'Edit "' + self.object.name + '"'
        return context


class SurveyAdd(CreateView):
    model = Survey
    form_class = SurveyForm
    template_name = 'surveyer/edit.html'

    def get_context_data(self, **kwargs):
        context = super(SurveyAdd, self).get_context_data(**kwargs)
        context['title'] = "Add new Survey"
        return context


class SurveyDelete(DeleteView):
    model = Survey
    success_url = reverse_lazy('surveys')
    template_name = 'confirm_delete.html'