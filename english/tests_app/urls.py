from django.urls import path
from . import views

app_name = "tests_app"

urlpatterns = [
    path('<slug:slug>/', views.test_detail, name='detail'),
    path('<slug:slug>/submit/', views.test_submit, name='submit'),
]