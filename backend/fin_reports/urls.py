from django.conf.urls import url
from fin_reports import views

urlpatterns = {
    url(r'upload', views.upload),
    url(r'show_fin', views.show_fin_reports),
    url(r'reports', views.fin_reports),
}
