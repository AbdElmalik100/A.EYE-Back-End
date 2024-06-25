# Generated by Django 4.2.9 on 2024-05-07 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_patientdetectionresults_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctordetectionresults',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_patients_detections', to='api.patients'),
        ),
    ]
