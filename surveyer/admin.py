from django.contrib import admin
from surveyer.models import *


# Register your models here.
class QuestionInline(admin.TabularInline):
    model = Survey.questions.through
    extra = 1


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [QuestionInline]

admin.site.register(Question)