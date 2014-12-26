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


def record_edit(request, record_id=None):
    if record_id:
        record = Record.objects.get(id=record_id)
        title = 'Edit record "' + str(record.id) + '"'
    else:
        title = 'Add new Record'

    if request.method == 'POST':
        if record_id:
            form = RecordForm(request.POST, instance=record)
        else:
            form = RecordForm(request.POST)

        if form.is_valid():
            record = form.save()
            return redirect('record-details', record.id)
    else:
        if record_id:
            form = RecordForm(instance=record)
        else:
            form = RecordForm()

    return render(request, 'records/edit.html', {
        'form': form,
        'title': title
        })


def record_delete(request):
    pass