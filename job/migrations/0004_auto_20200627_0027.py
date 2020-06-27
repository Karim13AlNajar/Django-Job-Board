# Generated by Django 3.0.7 on 2020-06-26 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_auto_20200627_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='jobType',
            field=models.CharField(choices=[('Full-time', 'F-T'), ('Part-time', 'P-T'), ('Freelancer', 'F')], max_length=15),
        ),
    ]