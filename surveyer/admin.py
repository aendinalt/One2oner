from django.contrib import admin
from django.forms.extras import widgets
from surveyer.models import *
from records.admin import Answer


# Register your models here.
class QuestionInline(admin.TabularInline):
    model = Survey.questions.through
    extra = 1


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    filter_horizontal = ['questions']
    prepopulated_fields = {'slug': ('name',)}

    list_display = ['name', 'number_of_questions']

    def number_of_questions(self, obj):
        questions = obj.questions.all()
        num = len(questions)
        return 'Questions: ' + str(num)


class AnswerInline(admin.TabularInline):
    model = Answer
    fk_name = 'question'
    extra = 1
    radio_fields = {'mark': admin.HORIZONTAL}


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ['__unicode__', 'get_surveys']
    search_fields = ['question_text']

