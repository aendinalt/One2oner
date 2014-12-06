from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    package = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name + ' ' + self.surname