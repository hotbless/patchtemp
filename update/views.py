from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from targethost.models import UpdateInfo

from django_tables2 import SingleTableView
from .tables import UpdateTable



from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets




class SSHTargetButton(viewsets.ViewSet):
    # template_name = 'update/button.html'

    def request_page(self, request):
        if request.method == 'post':
            if request.GET.get('mybtn'):
                request.GET.get('mytextbox')
                return Response({"message": "POST Info is: "} + str(request), status=999)
                # return render(request, 'button.html', status=700)


class TargetHostInfo(viewsets.ViewSet):
    def current_host_info(self, request):
        host_ip_var = None
        if 'host_ip' in request.session:
            host_ip_var = request.session['host_ip']
            # del request.session['host_ip']
        # host_ip = (request.GET.get('host_ip'))
        if host_ip_var:
            return render(request, 'update/test.html', {'host_ip': host_ip_var})
        else:
            host_ip_var = ''
            return render(request, 'update/test.html', {'host_ip': host_ip_var})


# class UpdateInfoListView(ListView):
class UpdateInfoListView(SingleTableView):
    model = UpdateInfo
    table_class = UpdateTable
    table_pagination = {"per_page": 8, }
    template_name = 'update/update.html'








