<<<<<<< HEAD
# Generated by Django 5.0 on 2024-01-05 21:56
=======
# Generated by Django 5.0 on 2024-01-05 21:24
>>>>>>> 2091af7fb5410523961ec2c1922506a6d911165f

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('field_of_study', '0001_initial'),
        ('professors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialisations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='field_of_study.fieldofstudy')),
                ('professors', models.ManyToManyField(to='professors.professors')),
            ],
        ),
    ]
