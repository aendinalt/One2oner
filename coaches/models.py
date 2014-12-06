from django.db import models

roles = (
    ('Instructor', 'Instructor'),
    ('Assistant', 'Assistant'),
)


class Coach(models.Model):

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    role = models.CharField(max_length=50, choices=roles)
    course = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name + ' ' + self.surname