# Generated by Django 5.1.4 on 2025-03-01 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tts', '0002_requestmp3_audio_file_requestmp3_text_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestmp3',
            name='audio_file',
            field=models.FileField(blank=True, storage='audio', upload_to=''),
        ),
    ]
