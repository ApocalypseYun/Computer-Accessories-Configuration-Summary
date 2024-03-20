from django.urls import path
from compare import views

urlpatterns = [
    path(r'compare/', views.index)
]