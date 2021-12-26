from django.conf.urls import url
from ledger import views

urlpatterns = {
    url(r'pre_sales', views.pre_sales),

}
