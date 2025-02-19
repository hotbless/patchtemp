"""grindstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from installed.views import InstalledListView
from update.views import UpdateInfoListView
from sshtarget.views import SSHTarget
from targethost.views import TargetHost
from update.views import SSHTargetButton, TargetHostInfo
from sshtarget.views import Login
from testdatatable.views import test_datatables2_view

urlpatterns = [
    # path('installed/', include('installed.urls')),
    path('admin/', admin.site.urls),
    path("installed/", InstalledListView.as_view()),
    path("update/", UpdateInfoListView.as_view()),
    # path('update/^?P<host_ip>/$', UpdateInfoListView.as_view(), name='update_info_table'),
    # path("update/test", TargetHostInfo.as_view({'get': 'current_host_info'}), name='update_info_table'),
    path("update/test", TargetHostInfo.as_view({'get': 'current_host_info'})),
    path("restry/", include('restry.urls')),
    path("sshtarget/", SSHTarget.as_view({'get': 'chk_host'})),
    # path("targethost/", TargetHost.as_view()),
    path("targethost/check", TargetHost.as_view({'get': 'chk_host'})),
    path("targethost/query", TargetHost.as_view({'get': 'query_installed'})),
    path("sshtarget/trialtest", Login),
    path("do/do", test_datatables2_view),
    # path("targethost/host", TargetHost.as_view({'get': 'connect_host'})),
    # path("targethost/host", TargetHost.as_view({'get': 'connect_host'})),
    path("targethost/host", TargetHost.as_view({'get': 'connect_host', 'post': 'connect_host'})),
    #path(r'^update/(?P<host_ip>[^\/]*)/$', TargetHost.connect_host, name='host_ip'),
    # path(r'^update/quest/$', SSHTarget.as_view({'post': 'request_page'})),

    # path("ssh_target/", include('sshtarget.urls')),
]
