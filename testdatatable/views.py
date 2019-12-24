from django.shortcuts import render

# Create your views here.
from targethost.models import UpdateInfo


def test_datatables2_view(request):
    # table_list = UpdateInfo.objects.order_by('NAME')
    table_list = UpdateInfo.objects.all()

    context_table = {'table_list': table_list}

    return render(request, 'testdatatable/testdatatable.html', context_table)