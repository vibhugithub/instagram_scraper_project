from django.db import models

from datetime import datetime


class InstagramDownload(models.Model):
    link = models.CharField(max_length=200)
    caption = models.TextField(blank=True)  # Allow blank caption
    like = models.TextField(blank=True)
    # comments = models.PositiveIntegerField(default=0)
    username = models.CharField(max_length=100)
    date = models.TextField(blank=True)

    def __str__(self):
        return self.link
