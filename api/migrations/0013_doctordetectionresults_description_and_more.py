# Generated by Django 4.2.9 on 2024-05-07 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_doctordetectionresults_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctordetectionresults',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctordetectionresults',
            name='points',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctordetectionresults',
            name='result_class',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctordetectionresults',
            name='result',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]