from django.db import models

tech = (
    ('Python', 'Python'),
    ('Ruby', 'Ruby'),
    ('JavaScript', 'JavaScript'),
)


class Course(models.Model):

    technology = models.CharField(max_length=255, choices=tech)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    instructor = models.CharField(max_length=255)
    assistant = models.CharField(max_length=255)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __unicode__(self):
        return self.technology + ' | ' + self.name
