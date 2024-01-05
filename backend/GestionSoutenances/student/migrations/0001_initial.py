# Generated by Django 5.0 on 2024-01-05 22:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('field_of_study', '0001_initial'),
        ('school_year', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familyName', models.CharField(max_length=50)),
                ('firstName', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
                ('birth_date', models.DateField(default=None)),
                ('field_of_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='field_of_study.fieldofstudy')),
                ('school_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_year.schoolyear')),
            ],
        ),
    ]
