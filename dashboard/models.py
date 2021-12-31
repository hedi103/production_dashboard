from django.db import models

class Ems(models.Model):
    id = models.IntegerField(primary_key=True)
    hourfc = models.IntegerField(blank=True, null=True)
    humidity = models.IntegerField(db_column='Humidity', blank=True, null=True)  # Field name made lowercase.
    pressure = models.IntegerField(db_column='Pressure', blank=True, null=True)  # Field name made lowercase.
    temperature = models.DecimalField(db_column='Temperature', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dew_point = models.DecimalField(db_column='Dew_point', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ems'