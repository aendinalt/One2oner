from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Record(models.Model):
    interviewer = models.ForeignKey(User, related_name='interviewer')
    employee = models.ForeignKey(User, related_name='employee')
    survey = models.ForeignKey('surveyer.Survey')
    date = models.DateField()

    def __unicode__(self):
        return str(self.employee) + ' | ' + str(self.date)


class Answer(models.Model):
    record = models.ForeignKey(Record)
    question = models.ForeignKey('surveyer.Question')
    mark = models.CharField(max_length=10, choices=(
        ('G', ':-)'),
        ('N', ':-|'),
        ('B', ':-('),
    ))
    explanation = models.TextField(max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return '- ' + self.question.__unicode__() + '\n' + '- ' + self.get_mark_display()