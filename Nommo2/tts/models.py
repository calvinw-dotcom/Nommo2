from django.db import models
from django.contrib.auth.models import User





class RequestMp3(models.Model):
    
    title = models.CharField(max_length=200,blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    requested_url = models.CharField(max_length=200, blank=True, null=True)
    text_file = models.FileField(blank=True)
    audio_file = models.FileField(upload_to="mp3_files/", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


def get_text(self, line):
    pass