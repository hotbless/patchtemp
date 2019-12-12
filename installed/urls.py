from django.urls import path

from . import views

from django.contrib import admin

from installed.views import PackagesListView

urlpatterns = [
    path('', views.installed, name='installed'),
    path("packages/", PackagesListView.as_view())
]
