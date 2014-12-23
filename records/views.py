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
    title = 'Edit record "' + str(record.id) + '"'
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        answer_formset = AnswerFormSet(request.POST,
                                       queryset=Answer.objects.
                                       filter(record__id=record_id))
        if form.is_valid() and answer_formset.is_valid():
            record = form.save()
            answer_formset.save()
            return redirect('record-details', record.id)
    else:
        form = RecordForm(instance=record)
        answer_formset = AnswerFormSet(
            queryset=Answer.objects.filter(record__id=record_id),
            initial=[{
               'record': record,
            }])

    return render(request, 'records/edit.html', {
        'record': record,
        'answer_formset': answer_formset,
        'form': form,
        'title': title
        })