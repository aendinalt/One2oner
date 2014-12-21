from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.TextField(max_length=1000)

    def get_surveys(self):
        return "\n".join([k.name for k in self.survey_set.all()])

    def __unicode__(self):
        return self.question_text


class Survey(models.Model):
    name = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)

    def __unicode__(self):
        return self.name[:50]