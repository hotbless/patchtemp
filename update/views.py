from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from targethost.models import UpdateInfo

from django_tables2 import SingleTableView
from .tables import UpdateTable


from django_tables2 import MultiTableMixin
from django.views.generic.base import TemplateView


# class UpdateInfoListView(ListView):
class UpdateInfoListView(SingleTableView):
    model = UpdateInfo
    table_class = UpdateTable
    table_pagination = {"per_page": 10, }
    template_name = 'update/update.html'
