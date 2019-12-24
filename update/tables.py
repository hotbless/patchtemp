from django_tables2 import TemplateColumn
import django_tables2 as tables
from targethost.models import UpdateInfo
from update import views
import itertools


# class UpdateTable(tables.Table):
#
#     class Meta:
#
#         model = UpdateInfo
#         template_name = "django_tables2/bootstrap.html"
#         fields = ("NAME", "VERSION", "ARCH", "REPO")

class CustomTemplateColumnGetName(tables.TemplateColumn):
    def render(self, record, table, value, bound_column, **kwargs):
        if str(record.REPO) != "updates":
            return '------'
        else:
            return super(CustomTemplateColumnGetName, self).render(record, table, value, bound_column, **kwargs)


# class SummingColumn(tables.Column):
#     def render_footer(self, bound_column, table):
#         return sum(bound_column.accessor.resolve(row) for row in table.data)


class UpdateTable(tables.Table):
    # pkg_name = tables.Column(verbose_name="Package Name")
    # pkg_ver = tables.Column(verbose_name="Version")
    # pkg_arch = tables.Column(verbose_name="Arch")
    # pkg_repo = tables.Column(verbose_name="Repo")

    def __init__(self, *args, **kwargs):
        super(UpdateTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()

    # age = tables.Column(attrs={"tf": {"bgcolor": "red"}})
    TIME = tables.DateTimeColumn(format='Y-m-d， h:i:s', orderable=False)
    warning = tables.Column(attrs={"td": {"class": "table-danger"}})
    info = tables.Column(attrs={"tf": {"class": "bg-danger"}})


    class Meta:
        # attrs = {'class': 'paleblue'}
        attrs = {'class': 'table table-striped table-hover', 'id': 'hahaha'}
        # attrs = {"th": "thread-dark"}

        model = UpdateInfo
        # template_name = "django_tables2/bootstrap4.html"
        # template_name = "update/static/bootstrap.min.css"
        fields = ("NAME", "VERSION", "ARCH", "REPO", "Detail")
        template_name = "update/table.html"


    # if record.REPO != 'base':
    Detail = CustomTemplateColumnGetName(template_name="update/detail.html", orderable=False)


    # Collapse = tables.TemplateColumn(template_name="update/collapse.html", orderable=False)
    # def render_repo(self, value, record):
    #     return mark_safe('''<a href=%s>%s</a>''' % (record.REPO, value)

    # Detail = tables.TemplateColumn('<a class="btn btn-info btn-sm" href="www.263.com">Open</a>')
    # Detail = "0"
    #if REPO != 'base':
        # Detail = tables.TemplateColumn(template_name="update/detail.html")

    # def render_REPO(self, value, column):
    #     column.attrs = {'td': {'bgcolor': 'orange'}}
    #     if value != 'base':
    #         # Detail = tables.TemplateColumn(template_name="update/detail.html")
    #         return "<%s>--" % value
    #
    # # DETAIL = tables.TemplateColumn(template_name="update/detail.html")
    #
    # def render_DETAIL(self, value, column):
    #     column.attrs = {'td': {'bgcolor': 'grey'}}
    #     if value != 'Base':
    #         tables.TemplateColumn('<a class="btn btn-info btn-sm" href="www.263.com">Open</a>')
    #         # return value
    #     else:
    #         return "---"
        #

    # def column_test(self):
    #     if self.render_REPO() != "base":
    #         self.Detail = tables.TemplateColumn('<a class="btn btn-info btn-sm" href="www.263.com">Open</a>')
    # def render_Detail(self, column):
    #     column.attrs = {'td': {'bgcolor': 'darkblue'}}
    #     # repo_value = self.render_REPO()
    #     # if repo_value != "base":
    #     #     tables.TemplateColumn(template_name="update/detail.html")


    # def render_REPO(self, value):
    #     if value == "base":
    #         Detail = tables.TemplateColumn(template_name="update/detail.html")
    #     return "<%s>++" % value



    # new_database = tables.CheckBoxColumn()







