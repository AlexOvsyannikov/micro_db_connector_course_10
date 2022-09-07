from django.urls import path

from . import views

urlpatterns = [
    path('', views.GuestConnector.as_view(), name='index'),
]