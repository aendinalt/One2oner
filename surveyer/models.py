from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.TextField(max_length=1000)

    def __unicode__(self):
        return Question.question_text[:50]


class Survey(models.Model):
    name = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)

    def __unicode__(self):
        return Survey.name[:50]


class Answer(models.Model):
    mark = models.CharField(max_length=10, choices=(
        ('G', ':-)'),
        ('N', ':-|'),
        ('B', ':-('),
    ))
    explanation = models.TextField(max_length=1000, null=True, blank=True)
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return Answer.mark + ' ' + Answer.question.__unicode__()