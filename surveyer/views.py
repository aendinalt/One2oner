from django.shortcuts import render

# Create your views here.


def surveys_list(request):
    return render(request, 'surveyer/list.html', {})