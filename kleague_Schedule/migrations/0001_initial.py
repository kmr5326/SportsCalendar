# Generated by Django 3.0.5 on 2021-06-03 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('date', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('game1', models.CharField(max_length=50, null=True)),
                ('game2', models.CharField(max_length=50, null=True)),
                ('game3', models.CharField(max_length=50, null=True)),
                ('game4', models.CharField(max_length=50, null=True)),
                ('game5', models.CharField(max_length=50, null=True)),
                ('game6', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
