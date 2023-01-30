from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('history', views.history, name='history'),
    path('impression', views.impression, name='impression'),
    path('admin/', admin.site.urls),
]
