from django.db import models

class production_pvrmt(models.Model):
    id = models.AutoField(primary_key=True)
    dt_utc = models.DateTimeField()
    charge = models.FloatField(db_column='charge')
    decharge = models.FloatField(db_column='decharge')

    class Meta:
        managed = True
        db_table = 'production_pvrmt'