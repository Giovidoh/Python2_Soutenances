# Generated by Django 5.0 on 2024-01-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defense', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defenseprofessor',
            name='mark',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
