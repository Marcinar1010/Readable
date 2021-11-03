from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Authors(models.Model):
    name = models.TextField()
    year = models.PositiveIntegerField()

class books(models.Model):
    google_id = models.CharField(max_length=30)
    title = models.TextField()
    author = models.ForeignKey(Authors, on_delete=models.PROTECT)
    review = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=2)