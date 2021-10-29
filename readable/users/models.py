from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'