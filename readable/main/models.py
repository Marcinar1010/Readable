from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class books(models.Model):
    title = models.TextField()
    author = models.TextField()
    review = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    