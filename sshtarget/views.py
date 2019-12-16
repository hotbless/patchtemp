from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View

from fabric import Connection
from GetConfig import GetConfig
# from DbOp import DbOp

from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


class ConnectTarget:
    def __init__(self):
        self.conf = GetConfig().get_config()
        self.target_host = self.conf.get('target_host')
        # print(self.target_host)
        self.target_host_ip = self.target_host.get('ip')
        self.target_host_port = self.target_host.get('port')
        self.target_host_user = self.target_host.get('user')
        self.target_host_pwd = self.target_host.get('pwd')
        # self.db_inst = DbOp()
        # self.db_inst.create_installed_table()
        # self.db_inst.create_update_table()

    def connect(self):
        connect = Connection(
            host=self.target_host_ip,
            # host='1.1.1.1',
            port=self.target_host_port,
            user=self.target_host_user,
            connect_kwargs={
                "password": self.target_host_pwd,
            },
            connect_timeout=10
        )
        status = False
        try:
            connect.open()
        except Exception:
            # raise TimeoutError("SSH connection failed !")
            # status = False
            raise Exception("SSH connection failed !")
            status = False
        else:
            status = True
        finally:
            connect.close()
            return connect, status


# class SSHTarget(View):
#     def connect_host(self, request):
#         connect, status = ConnectTarget().connect()
#         if status is False:
#             return HttpResponse("Can't access Target host", status=406)
#         return connect

@api_view()
def connect_host(request):
    connect, status = ConnectTarget().connect()
    if status is False:
        return HttpResponse("Can't access Target host", status=406)
    return Response({"message": "Test restful api "}, status=200)
