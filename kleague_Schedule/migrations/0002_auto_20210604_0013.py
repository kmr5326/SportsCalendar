# Generated by Django 3.0.5 on 2021-06-03 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kleague_Schedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='date',
            new_name='_id',
        ),
    ]