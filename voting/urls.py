from django.urls import path
from . import views

app_name = 'voting'

urlpatterns = [
    path('', views.voting_list, name='list'),
    path('<int:pk>/', views.voting_detail, name='detail'),
    path('<int:pk>/vote/', views.cast_vote, name='vote'),
    path('<int:pk>/results/', views.voting_results, name='results'),
]
