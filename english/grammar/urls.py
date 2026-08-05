from django.urls import path
from . import views

app_name = "grammar"

urlpatterns = [
    path('', views.topic_list, name='list'),
    path('<slug:slug>/', views.topic_detail, name='detail'),
]