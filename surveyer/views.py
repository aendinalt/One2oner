from django.shortcuts import render
from models import *

# Create your views here.


def surveys_list(request):
    surveys = Survey.objects.all()
    return render(request, 'surveyer/list.html', {'surveys': surveys})


def survey_details(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    questions = Question.objects.filter(survey__id=survey_id)
    print questions
    return render(request, 'surveyer/item.html', {
        'survey': survey,
        'questions': questions
        })


def survey_edit(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    questions = Question.objects.filter(survey__id=survey_id)
    return render(request, 'surveyer/item.html', {
        'survey': survey,
        'questions': questions
        })
