from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import ListView
from .models import installed_info_sql


def installed(request):
    return HttpResponse("Host installed packages info page.")


class PackagesListView(ListView):
    model = installed_info_sql()
    template_name = 'installed/packages.html'
