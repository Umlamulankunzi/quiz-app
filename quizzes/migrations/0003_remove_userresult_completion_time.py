# Generated by Django 4.2.15 on 2024-08-17 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresult',
            name='completion_time',
        ),
    ]
