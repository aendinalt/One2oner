from django.db import models

packages = (
    ('Standart', 'Standart'),
    ('Gold', 'Gold'),
    ('VIP', 'VIP'),
)


class Student(models.Model):

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    package = models.CharField(max_length=15, choices=packages)

    def __unicode__(self):
        return self.name + ' ' + self.surname