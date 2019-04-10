from . import views
from django.urls import path

urlpatterns = [

    path('', views.comments, name="comments"),


]