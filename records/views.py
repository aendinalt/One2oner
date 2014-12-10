from django.shortcuts import render
from models import *


# Create your views here.
def records_list(request):
    records = Record.objects.all()
    return render(request, 'records/list.html', {'records': records})


def record_details(request, record_id):
    pass
