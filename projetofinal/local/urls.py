from django.urls import path

from . import views

urlpatterns = [
    path('', views.local),
    path('ondeestamos/', views.ondeestamos),
    path('local/', views.local),
]