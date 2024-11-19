from account.views import RegisterView,Login
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',Login.as_view())
]