from django.urls import path
from . import views
from .views import csv_upload

urlpatterns = [
    path('events/', views.event_list, name='event_list'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/details/<int:id>', views.event_detail, name='event_detail'),
    path('events/update/<int:id>/', views.event_update, name='event_update'),
    path('events/delete/<int:id>/', views.event_delete, name='event_delete'),
    path('events/import/', views.import_csv, name='import_csv'),
    path('attendees/register/', views.register_attendee, name='register_attendee'),
    path('attendees/update/<int:id>/', views.update_attendee, name='update_attendee'),
    path('attendees/register/event_attendees.html', views.event_attendees, name='event_attendees'),
    path('upload_csv/', csv_upload, name='csv_upload'),]


