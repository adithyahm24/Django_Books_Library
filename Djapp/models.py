from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, blank=True, null=True)
    file = models.FileField(upload_to='')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
