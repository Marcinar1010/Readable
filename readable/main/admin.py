from django.contrib import admin
from main.models import Book, ReadingStatus, ReadingProgress

admin.site.register(Book)
admin.site.register(ReadingStatus)
admin.site.register(ReadingProgress)