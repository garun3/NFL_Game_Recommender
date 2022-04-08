# Generated by Django 4.0.2 on 2022-02-23 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField(default=0)),
                ('day', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('winner', models.CharField(max_length=200)),
                ('home', models.CharField(max_length=200)),
                ('loser', models.CharField(max_length=200)),
                ('PtsW', models.IntegerField(default=0)),
                ('PtsL', models.IntegerField(default=0)),
                ('YdsW', models.IntegerField(default=0)),
                ('TOW', models.IntegerField(default=0)),
                ('YdsL', models.IntegerField(default=0)),
                ('TOL', models.IntegerField(default=0)),
            ],
        ),
    ]
