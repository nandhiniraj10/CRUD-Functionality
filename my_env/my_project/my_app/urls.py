from django.urls import path
from . import views
from .views import (candidate_list,candidate_detail,candidate_delete,candidate_update,candidate_create)

urlpatterns = [
    path('', views.candidate_list, name='candidate_list'),
    path('create/', views.candidate_create, name='candidate_create'),
    path('<int:pk>/', views.candidate_detail, name='candidate_detail'),
    path('<int:pk>/update/', views.candidate_update, name='candidate_update'),
    path('<int:pk>/delete/', views.candidate_delete, name='candidate_delete'),
]
