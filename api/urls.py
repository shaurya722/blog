from account.views import RegisterView
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('account/',include('account.urls') ),
    path('home/',include('home.urls'))
]