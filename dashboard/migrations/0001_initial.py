# Generated by Django 3.2.5 on 2021-07-05 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='production_pvrmt',
            fields=[
                ('dt_utc', models.DateTimeField(primary_key=True, serialize=False)),
                ('Charge', models.FloatField(db_column='charge')),
                ('Decharge', models.FloatField(db_column='decharge')),
            ],
            options={
                'db_table': 'production_pvrmt',
                'managed': True,
            },
        ),
    ]
