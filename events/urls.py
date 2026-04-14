from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.events_list, name='list'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('<int:pk>/', views.event_detail, name='detail'),
]
