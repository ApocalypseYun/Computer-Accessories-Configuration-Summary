from django.urls import path
from login import views

urlpatterns = [
    path(r'login_hello/', views.index)
]