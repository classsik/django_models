from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('news/add/', add_news, name='add_news'),
    path('news/edit/<int:pk>/', edit, name='edit'),
    path('news/delete/<int:pk>/', delete, name='delete'),
]
