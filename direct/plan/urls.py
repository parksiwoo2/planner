from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name="calendar_view"),
    path('event/<int:event_id>/', views.event_detail, name="event_detail"),
    path('event/new/', views.event_create, name="event_create"),
]