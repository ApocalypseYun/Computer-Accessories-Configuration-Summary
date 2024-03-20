from django.urls import path
from hardware import views

urlpatterns = [
    path(r'hardware/', views.index)
]