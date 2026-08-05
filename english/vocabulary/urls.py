from django.urls import path
from . import views

app_name = "vocabulary"

urlpatterns = [
    path('', views.set_list, name='list'),
    path('<slug:slug>/', views.set_detail, name='detail'),
]