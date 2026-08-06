from django.urls import path
from . import views

app_name = "vocabulary"

urlpatterns = [
    path('', views.set_list, name='list'),
    path('my/', views.my_sets, name='my_sets'),
    path('new/', views.set_create, name='create'),
    path('<slug:slug>/', views.set_detail, name='detail'),
    path('<slug:slug>/edit/', views.set_edit, name='edit'),
    path('<slug:slug>/delete/', views.set_delete, name='delete'),
    path('<slug:slug>/words/add/', views.word_add, name='word_add'),
    path('<slug:slug>/words/<int:word_id>/delete/', views.word_delete, name='word_delete'),
]