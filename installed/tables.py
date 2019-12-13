import django_tables2 as tables
from .models import InstalledInfo


class InstalledInfoTable(tables.Table):
    attrs = {'class': 'table'}
    class Meta:
        model = InstalledInfo
        template_name = "django_tables2/bootstrap.html"
        fields = ("NAME", "VERSION", "ARCH")
