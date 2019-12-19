from django.urls import path

from . import views
from update.views import SSHTarget

# from django.contrib import admin

# from installed.views import PackagesListView

app_name = 'update'

urlpatterns = [
    # path('', views.installed, name='installed'),
    path('', views.UpdateInfoListView, name='update'),

    # path("packages/", PackagesListView.as_view())
]
