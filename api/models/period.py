from django.db import models

class Period(models.Model):
    menstruation = models.BooleanField(default=False)
    start_date = models.DateTimeField(default=None, null=True)
    end_date = models.DateTimeField(default=None, null=True)
    cycle_length = models.IntegerField(default=28)