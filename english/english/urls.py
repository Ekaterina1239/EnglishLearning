from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lessons.urls')),
    path('grammar/', include('grammar.urls')),
    path('vocabulary/', include('vocabulary.urls')),
    path('reading/', include('reading.urls')),
    path('tests/', include('tests_app.urls')),
    path('accounts/', include('users.urls')),
]