from django.urls import path
from . import views

urlpatterns = [
    path('', views.BaseReview.as_view(), name='base_review'),
]
