from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_url, name='shorten_url'),
    path('<str:short_url>/', views.redirect_url, name='redirect_url'),
    path('update/<str:short_url>/', views.update_url, name='update_url'),
    path('delete/<str:short_url>/', views.delete_url, name='delete_url'),
    path('statistics/<str:short_url>/', views.statistics, name='statistics'),
]