from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_page, name='dashboard'),
    path('upload/', views.upload_page, name='upload_page'),
]