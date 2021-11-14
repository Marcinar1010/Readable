from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='main-home'),
    path('about/', views.about, name='main-about'),
    path('library/', views.library, name='main-library'),
    path('reading_status', views.reading_status, name="main-reading-status"),
    path('bookshelf/', views.bookshelf, name="main-bookshelf")
]