from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from targethost.models import UpdateInfo

from django_tables2 import SingleTableView
from .tables import UpdateTable


# class UpdateInfoListView(ListView):
class UpdateInfoListView(SingleTableView):
    model = UpdateInfo
    table_class = UpdateTable
    template_name = 'update/update.html'
