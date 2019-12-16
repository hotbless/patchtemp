from django.urls import path
from sshtarget.views import SSHTarget
from . import views


urlpatterns = [
    path('', SSHTarget.as_view(), name='sshtarget'),
    # path('', views.connect_host, name='ssh_target'
]
