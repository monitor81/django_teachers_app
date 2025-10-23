from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('disciplines/', views.discipline_list, name='discipline_list'),
]