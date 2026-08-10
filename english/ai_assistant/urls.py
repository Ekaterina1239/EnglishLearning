from django.urls import path
from . import views

app_name = "ai_assistant"

urlpatterns = [
    path('explain-mistakes/', views.explain_last_mistakes, name='explain_mistakes'),
]