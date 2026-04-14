from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    path('', views.materials_list, name='list'),
    path('<int:pk>/', views.material_detail, name='detail'),
]
