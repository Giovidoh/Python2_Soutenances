# Generated by Django 5.0 on 2024-01-05 22:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('professors', '0001_initial'),
        ('rooms', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel( 
            name='Defense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField(default=None)),
                ('result', models.IntegerField(default=None)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.rooms')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='DefenseProfessor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(default=None)),
                ('defense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='defense.defense')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professors.professors')),
            ],
        ),
        migrations.AddField(
            model_name='defense',
            name='professors',
            field=models.ManyToManyField(through='defense.DefenseProfessor', to='professors.professors'),
        ),
    ]
