from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponseRedirect

from fabric import Connection
from GetConfig import GetConfig
from DbOp import DbOp

from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import InstalledInfo
from update.views import UpdateInfoListView, TargetHostInfo
from installed.views import InstalledListView

from PyOp.TargetOp import TargetOp



# Create your views here.


# class TargetOp:
#     def __init__(self):
#         self.conf = GetConfig().get_config()
#         self.target_host = self.conf.get('target_host')
#         # print(self.target_host)
#         self.target_host_ip = self.target_host.get('ip')
#         self.target_host_port = self.target_host.get('port')
#         self.target_host_user = self.target_host.get('user')
#         self.target_host_pwd = self.target_host.get('pwd')
#         self.db_inst = DbOp()
#         self.db_inst.create_installed_table()
#         self.db_inst.create_update_table()
#
#     def conditional_decorator(self, condition):
#         def decorator(func):
#             if not condition:
#                 return func
#         return decorator
#
#     def connect(self):
#         connect = Connection(
#             host=self.target_host_ip,
#             # host='1.1.1.1',
#             port=self.target_host_port,
#             user=self.target_host_user,
#             connect_kwargs={
#                 "password": self.target_host_pwd,
#             },
#             connect_timeout=5
#         )
#         return connect
#
#     def chk_connect(self):
#         status = False
#         connect_hdle = self.connect()
#         try:
#             connect_hdle.open()
#         except Exception:
#             # raise TimeoutError("SSH connection failed !")
#             # status = False
#             raise Exception("SSH connection failed !")
#             status = False
#         else:
#             status = True
#         finally:
#             connect_hdle.close()
#             return status
#
#     def connect_mod(self, ip, password):
#         connect = Connection(
#             host=ip,
#             # host='1.1.1.1',
#             port=22,
#             user='root',
#             connect_kwargs={
#                 "password": password,
#             },
#             connect_timeout=5
#         )
#         return connect
#
#     def chk_connect_mod(self, ip, password):
#         status = False
#         connect_hdle = self.connect_mod(ip, password)
#         try:
#             connect_hdle.open()
#         except Exception:
#             # raise TimeoutError("SSH connection failed !")
#             # status = False
#             raise Exception("SSH connection failed !")
#             status = False
#         else:
#             status = True
#         finally:
#             connect_hdle.close()
#             return status
#
#
#
#     def run_cmd(self, cmd, warn=False):
#         try:
#             result = self.connect().run(cmd, warn=warn)
#             # result = connect.run(r'rpm -qa --queryformat "%{NAME} %{EPOCH} %{VERSION} %{RELEASE} %{ARCH}\n"')
#             return result
#         except Exception as err:
#             raise err("Command execution Failed !")
#         finally:
#             self.connect().close()
#
#     def run_cmd_mod(self, ip, password, cmd, warn=False):
#         try:
#             if self.chk_connect_mod():
#                 result = self.connect_mod(ip, password).run(cmd, warn=warn)
#                 # result = connect.run(r'rpm -qa --queryformat "%{NAME} %{EPOCH} %{VERSION} %{RELEASE} %{ARCH}\n"')
#                 return result
#         except Exception as err:
#             raise err("Command execution Failed !")
#         finally:
#             self.connect().close()
#
#     def query_installed_pkg(self):
#         # info = self.run_cmd(r'rpm -qa --queryformat "%-60{NAME} %-12{EPOCH} %-25{VERSION} %-35{RELEASE} %-8{ARCH}\n"')
#         # info = self.run_cmd(r'rpm -qa --queryformat "%{NAME} %{EPOCH} %{VERSION} %{RELEASE} %{ARCH}\n"')
#         chk_words = ['Command exited with status', "stdout", '(no stderr)']
#         info = self.run_cmd('rpm -qa --queryformat "%{NAME} %{VERSION}-%{RELEASE} %{ARCH}\n"')
#         info = str(info)
#         if info:
#             list_info = info.split('\n')
#             for chk_word in chk_words:
#                 for each in list_info:
#                     if chk_word in each:
#                         list_info.remove(each)
#             list_info = [each for each in list_info if each != '']
#             if list_info:
#                 for index, each in enumerate(list_info):
#                     if each:
#                         dict_each = dict()
#                         list_each = each.split()
#                         dict_each = {
#                             'NAME': list_each[0],
#                             'VERSION': list_each[1],
#                             'ARCH': list_each[2]
#                         }
#                         # print(dict_each)
#                         list_info[index] = dict_each
#                         # self.db_inst.insert_installed_table(dict_each)
#                 # print(list_info)
#                 if list_info:
#                     # print(list_info)
#                     return list_info
#                 else:
#                     raise Exception('Get installed packages info failed !')
#
#     def installed_info_into_db(self):
#         pkg_info_list = self.query_installed_pkg()
#         # print(pkg_info_list)
#         try:
#             self.db_inst.insert_installed_info(pkg_info_list)
#         except Exception as err:
#             raise err("DB Operation Failed !")

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
    model = InstalledInfo

    def chk_host(self, request):
        status = TargetOp().chk_connect()
        if status is False:
            return Response({"message": "Can't access Target host new class"}, status=406)
        return Response({"message": "Connect Target host success new class"}, status=200)

    def query_installed(self, request):
        try:
            TargetOp().installed_info_into_db()
        except Exception as err:
            return Response({"message": "Query installed packages information Failed ! "}, status=406)
        else:
            return Response({"message": "Query installed packages information Success ! "}, status=200)

    def connect_host(self, request):
        if request.method == 'POST':
            # self.chk_host(request)
            op_host_ip = request.POST.get('host_ip')
            host_password = request.POST.get('host_password')
            target_host = TargetOp(op_host_ip, host_password)
            status = target_host.chk_connect()
            if status is False:
                return Response({"message": "Can't access Target host " + op_host_ip}, status=406)
            else:
                # if 'host_ip' in request.session:
                #     del request.session['host_ip']
                # response = redirect('/update/')
                # response = redirect('/update/?p=%s' % host_ip)
                # response = redirect('update_info_table', host_ip)
                target_host.installed_info_into_db()
                target_host.update_info_into_db()
                request.session['op_host_ip'] = op_host_ip
                response = redirect('/update/')
                # table = UpdateInfoListView.as_view()
                # response = render(request, 'update/update.html', {'host_ip': host_ip, 'table': table})
                return response
                # return Response({"message": "Connect Target host success " + host_ip}, status=200)
            # return Response({"message": "Can't access Target host"}, status=406, 'sshtarget/trialtest.html')
        else:
            return render(request, 'targethost/host.html')
