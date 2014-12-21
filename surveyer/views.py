from django.shortcuts import render, redirect
from models import *
from surveyer.forms import *

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
    title = 'Edit "' + survey.name + '"'
    if request.method == 'POST':
        form = SurveyForm(request.POST, instance=survey)
        if form.is_valid():
            survey = form.save()
            return redirect('survey-details', survey_id)
    else:
        form = SurveyForm(instance=survey)
    return render(request, 'surveyer/edit.html', {
        'survey': survey,
        'form': form,
        'title': title,
        })


def survey_add(request):
    title = "Add new Survey"
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save()
            return redirect('survey-details', survey.id)
    else:
        form = SurveyForm()
    return render(request, 'surveyer/edit.html', {
        'form': form,
        'title': title,
        })