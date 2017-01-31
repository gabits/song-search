from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Songs(models.Model):
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=512, null=True)
    song_name = models.CharField(max_length=512)
    lyrics = models.TextField(null=True)