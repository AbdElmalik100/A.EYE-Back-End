# Generated by Django 5.0.1 on 2024-02-12 23:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsapp', '0005_customuser_type_doctorprofile_patientprofile'),
        ('api', '0003_doctordetectionresults'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDetectionResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('result', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='detected_image')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_detections', to='accountsapp.patientprofile')),
            ],
        ),
    ]
