from django.urls import path
from . import views

app_name = 'gradebook'

urlpatterns = [
    path('', views.gradebook_index, name='index'),
    path('student/<int:pk>/', views.student_grades, name='student_grades'),
]
