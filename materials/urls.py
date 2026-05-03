from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'materials'

urlpatterns = [
    path('', MaterialListView.as_view(), name='list'),
    path('<int:pk>/', MaterialDetailView.as_view(), name='detail'),
    path('create/', MaterialCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', MaterialUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', MaterialDeleteView.as_view(), name='delete'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
]
