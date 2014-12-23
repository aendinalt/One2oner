from django.shortcuts import render, redirect
from models import *
from forms import *


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


def record_edit(request, record_id):
    record = Record.objects.get(id=record_id)
    answers = Answer.objects.filter(record__id=record_id)
    title = 'Edit record "' + str(record.id) + '"'
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            record = form.save()
            return redirect('record-details', record.id)
    else:
        form = RecordForm(instance=record)
    return render(request, 'records/edit.html', {
        'record': record,
        'answers': answers,
        'form': form,
        'title': title
        })