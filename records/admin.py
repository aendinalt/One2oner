from django.contrib import admin
from records.models import *


# Register your models here.
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):

    actions_on_top = True
    actions_on_bottom = True
    list_display = ['interviewer', 'employee', 'survey', 'date']
    ordering = ['employee']
    list_filter = ['employee', 'date']
    search_fields = ['employee']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    radio_fields = {'mark': admin.HORIZONTAL}

    actions_on_top = True
    actions_on_bottom = True
    list_display = ['record', '__unicode__', 'explanation']
    ordering = ['record']
    list_filter = ['record', 'record__date', 'mark']
    search_fields = ['__unicode__', 'explanation']