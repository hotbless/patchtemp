from django.urls import path
# from sshtarget.views import SSHTarget
from . import views


urlpatterns = [
    path('', views.connect_host, name='ssh_target'),
]
