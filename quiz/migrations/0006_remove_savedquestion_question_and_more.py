# Generated by Django 4.2.13 on 2024-06-09 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_savedquestion_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savedquestion',
            name='question',
        ),
        migrations.RemoveField(
            model_name='savedquestion',
            name='user',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
        migrations.DeleteModel(
            name='SavedQuestion',
        ),
    ]
