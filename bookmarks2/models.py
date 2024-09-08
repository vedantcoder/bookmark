from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone
from taggit.managers import TaggableManager
import requests
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save

class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    url = models.URLField('URL', default='')
    title = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default='', blank=True)
    opened = models.BooleanField()
    tag = TaggableManager()

    def __str__(self):
        return self.title if self.title else self.url

    class Meta:
        unique_together = ('url', 'user')

