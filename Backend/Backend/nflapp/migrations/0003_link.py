# Generated by Django 4.0.2 on 2022-03-30 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nflapp', '0002_rename_games_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similar_game', models.CharField(max_length=200)),
                ('box_score', models.CharField(max_length=400)),
                ('highlights', models.CharField(max_length=400)),
            ],
        ),
    ]
