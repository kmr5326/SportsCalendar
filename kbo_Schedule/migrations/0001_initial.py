# Generated by Django 3.0.5 on 2021-06-02 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('game1', models.CharField(max_length=20)),
                ('game2', models.CharField(max_length=20)),
                ('game3', models.CharField(max_length=20)),
                ('game4', models.CharField(max_length=20)),
                ('game5', models.CharField(max_length=20)),
            ],
        ),
    ]