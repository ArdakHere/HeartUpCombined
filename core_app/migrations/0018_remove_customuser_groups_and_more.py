# Generated by Django 5.0.3 on 2024-05-03 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0017_alter_customuser_managers'),
        ('machine_learning_app', '0007_remove_mldiagnosismodel_ecg_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='user',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
