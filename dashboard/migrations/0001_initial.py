# Generated by Django 3.2.5 on 2021-07-27 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='production_pvrmt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dt_utc', models.DateTimeField()),
                ('charge', models.FloatField(db_column='charge')),
                ('decharge', models.FloatField(db_column='decharge')),
            ],
            options={
                'db_table': 'production_pvrmt',
                'managed': True,
            },
        ),
    ]
