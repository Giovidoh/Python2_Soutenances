# Generated by Django 5.0 on 2024-01-22 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('field_of_study', '0003_fieldofstudy_date_deleting'),
        ('professors', '0002_professors_date_deleting_professors_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='professors',
            name='fieldOfStudy',
            field=models.ManyToManyField(to='field_of_study.fieldofstudy'),
        ),
    ]