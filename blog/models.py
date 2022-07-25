from django.conf import settings
from django.db import models

# Create your models here.
from django.db.models import CharField, TextField, DateTimeField, ForeignKey
from django.utils import timezone


class Article(models.Model):
    title = CharField(max_length=50)
    text = TextField()
    created = DateTimeField(auto_now_add=True)
    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)