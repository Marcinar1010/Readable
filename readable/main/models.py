from django.db import models
from django.db.models.fields import DateTimeField, TextField, PositiveSmallIntegerField
from django.db.models.fields.related import ManyToManyField
from django.db.models.lookups import IntegerGreaterThanOrEqual, YearLte
from django.utils import timezone
from django.contrib.auth.models import User

class Book(models.Model):
    google_id = models.CharField(max_length=30)
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    user = models.ManyToManyField(User, through="ReadingStatus")
    cover_url = models.TextField(null=True)
    info_url = models.TextField(null=True)
    authors = models.TextField(null=True)

    def __str__(self):
        return f"Nr: { self.id }  title: {self.title}"

class ReadingStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)

    LIST_TYPES = (
        ('T', 'To Read'),
        ('R', 'Reading'),
        ('H', 'Have Read'),
    )
    list_type = models.CharField(max_length=1, choices=LIST_TYPES)
    date_added = DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{ self.book } is in '{ self.get_list_type_display() } List' - User: { self.user.username }"

class ReadingProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    year_goal = PositiveSmallIntegerField(default=12)

    def __str__(self):
        return f"{ self.user.username }'s goal for this year: { self.year_goal }"
