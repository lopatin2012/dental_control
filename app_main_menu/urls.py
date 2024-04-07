from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainMenu.as_view(), name='base_review'),
]
