from django.db import models

class production_pvrmt(models.Model):
    dt_utc = models.DateTimeField(primary_key=True)
    charge = models.FloatField(db_column='charge')  # Field name made lowercase.
    decharge = models.FloatField(db_column='decharge')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'production_pvrmt'