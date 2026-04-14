from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.forum_index, name='index'),
    path('thread/<int:pk>/', views.thread_detail, name='thread_detail'),
]
