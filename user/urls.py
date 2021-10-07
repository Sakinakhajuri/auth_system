
from django.urls import path
from .views import listView,loginView
urlpatterns = [
    path('list',listView.as_view()),
path('login',loginView.as_view()),
    ]