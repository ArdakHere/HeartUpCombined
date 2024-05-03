# Generated by Django 5.0.3 on 2024-04-19 16:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0017_alter_customuser_managers'),
        ('machine_learning_app', '0005_mldiagnosismodel_ecg_mldiagnosismodel_heart_beat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mldiagnosismodel',
            name='echo_net_prediction',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mldiagnosismodel',
            name='echo_net_prediction_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='EchoNetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('echo_net_file', models.FileField(upload_to='echo_net_files/')),
                ('echo_net_file_upload_on', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.patient')),
            ],
        ),
        migrations.AddField(
            model_name='mldiagnosismodel',
            name='echo_net',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='machine_learning_app.echonetmodel'),
        ),
    ]
