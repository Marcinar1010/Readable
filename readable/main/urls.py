from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='main-home'),
    path('about/', views.about, name='main-about'),
    path('library/', views.library, name='main-library'),
    path('create_status', views.create_status, name="main-create-status"),
    path('delete_status/<status_id>', views.delete_status, name="main-delete-status"),
    path('bookshelf/', views.bookshelf, name="main-bookshelf"),
    path('update_status/<status_id>', views.update_status, name="main-update-status"),
    path('reco/', views.reco, name="main-reco"),
]