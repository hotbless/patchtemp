from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import ListView
from .models import InstalledInfo

from django_tables2 import SingleTableView

from .models import InstalledInfo
from .tables import InstalledInfoTable

# def installed(request):
#     return HttpResponse("Host installed packages info page.")


class InstalledListView(SingleTableView):
    model = InstalledInfo
    table_class = InstalledInfoTable
    template_name = 'installed/installed.html'
