from django.urls import path
from manager import views

urlpatterns = [
    path(r'manager/', views.index)
]