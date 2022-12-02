from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('history', views.history),
    path('impression', views.impression),
    path('photo_gallery', views.photo_gallery),
    path('admin/', admin.site.urls),
]
