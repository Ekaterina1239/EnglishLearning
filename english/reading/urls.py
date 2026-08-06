from django.urls import path
from . import views

app_name = "reading"

urlpatterns = [
    path('', views.text_list, name='list'),
    path('<slug:slug>/', views.text_detail, name='detail'),
]