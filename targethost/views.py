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
from rest_framework.views import APIView
from rest_framework import viewsets

# Create your views here.


class TargetOp:
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
        return connect

    def chk_connect(self):
        status = False
        connect_hdle = self.connect()
        try:
            connect_hdle.open()
        except Exception:
            # raise TimeoutError("SSH connection failed !")
            # status = False
            raise Exception("SSH connection failed !")
            status = False
        else:
            status = True
        finally:
            connect_hdle.close()
            return status

    def run_cmd(self, cmd, warn=False):
        try:
            result = self.connect().run(cmd, warn=warn)
            # result = connect.run(r'rpm -qa --queryformat "%{NAME} %{EPOCH} %{VERSION} %{RELEASE} %{ARCH}\n"')
            return result
        except Exception as err:
            raise err("Command execution Failed !")
        finally:
            self.connect().close()

    def query_installed_pkg(self):
        # info = self.run_cmd(r'rpm -qa --queryformat "%-60{NAME} %-12{EPOCH} %-25{VERSION} %-35{RELEASE} %-8{ARCH}\n"')
        # info = self.run_cmd(r'rpm -qa --queryformat "%{NAME} %{EPOCH} %{VERSION} %{RELEASE} %{ARCH}\n"')
        chk_words = ['Command exited with status', "stdout", '(no stderr)']
        info = self.run_cmd('rpm -qa --queryformat "%{NAME} %{VERSION}-%{RELEASE} %{ARCH}\n"')
        info = str(info)
        if info:
            list_info = info.split('\n')
            for chk_word in chk_words:
                for each in list_info:
                    if chk_word in each:
                        list_info.remove(each)
            list_info = [each for each in list_info if each != '']
            if list_info:
                for index, each in enumerate(list_info):
                    if each:
                        dict_each = dict()
                        list_each = each.split()
                        dict_each = {
                            'NAME': list_each[0],
                            'VERSION': list_each[1],
                            'ARCH': list_each[2]
                        }
                        # print(dict_each)
                        list_info[index] = dict_each
                        # self.db_inst.insert_installed_table(dict_each)
                # print(list_info)
                if list_info:
                    # print(list_info)
                    return list_info
                else:
                    raise Exception('Get installed packages info failed !')

# class SSHTarget(View):
    # def get(self, request):
    #     connect, status = ConnectTarget().connect()
    #     if status is False:
    #         return HttpResponse("Can't access Target host", status=406)
    #     return HttpResponse("Access Target host success", status=200)

# @api_view()
# def connect_host(request):
#     connect, status = ConnectTarget().connect()
#     if status is False:
#         return HttpResponse("Can't access Target host", status=406)
#     return Response({"message": "Connect Target Host Success "}, status=200)


class TargetHost(viewsets.ViewSet):
    def chk_host(self, request):
        status = TargetOp().chk_connect()
        if status is False:
            return Response({"message": "Can't access Target host new class"}, status=406)
        return Response({"message": "Connect Target host success new class"}, status=200)

    def query_installed(self, request):
        try:
            TargetOp().query_installed_pkg()
        except Exception as err:
            return Response({"message": "Query installed packages information Failed ! "}, status=406)
        else:
            return Response({"message": "Query installed packages information Success ! "}, status=200)

