from django.shortcuts import render
from models import *


# Create your views here.
def records_list(request):
    records = Record.objects.all()
    return render(request, 'records/list.html', {'records': records})


def record_details(request, record_id):
    record = Record.objects.get(id=record_id)
    answers = Answer.objects.filter(record__id=record_id)
    return render(request, 'records/item.html', {
        'record': record,
        'answers': answers,
        })
