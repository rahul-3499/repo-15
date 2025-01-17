from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField()
    fname = models.CharField(max_length=80)
    lname = models.CharField(max_length=80)
    marks = models.FloatField(max_length=80)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=80)

