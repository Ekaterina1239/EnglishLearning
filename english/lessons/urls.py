from django.urls import path
from . import views

app_name = "lessons"

urlpatterns = [
    path('', views.lesson_list, name='list'),
    path('<slug:slug>/', views.lesson_detail, name='detail'),
]