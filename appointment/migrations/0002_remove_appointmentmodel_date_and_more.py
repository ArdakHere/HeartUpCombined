# Generated by Django 5.0.3 on 2024-05-07 12:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentmodel',
            name='date',
        ),
        migrations.RemoveField(
            model_name='appointmentmodel',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='appointmentmodel',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='appointmentmodel',
            name='start_time',
        ),
        migrations.CreateModel(
            name='DoctorAvailabilityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_slot', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='appointmentmodel',
            name='slot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appointment.doctoravailabilitymodel'),
        ),
    ]