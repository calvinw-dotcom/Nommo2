# Generated by Django 5.1.4 on 2025-03-07 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tts', '0008_alter_requestmp3_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestmp3',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='mp3_files/'),
        ),
    ]
