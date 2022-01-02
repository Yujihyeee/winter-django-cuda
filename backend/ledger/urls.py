from django.conf.urls import url
from ledger import views

urlpatterns = {
    url(r'pre_sales', views.pre_sales),
    url(r'pre_cost', views.cost),
    url(r'up_sales', views.upload_sales),
    url(r'up_cost', views.upload_cost),
    url(r'profit', views.profit),
    url(r'report', views.report_process),
    url(r'6month', views.show_6month_cost),
    url(r'month_cost', views.month_cost),
    url(r'annual', views.year_profit),
    # url(r'sales/(?P<pk>\w{0,50})$', views.sales),
    url(r'sales', views.sales),
    url(r'insert', views.insert),
}
