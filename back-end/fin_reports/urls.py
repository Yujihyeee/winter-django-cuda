from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from fin_reports import views

urlpatterns = {
    url(r'pre', views.pre_process),
    url(r'upload', views.upload),
    url(r'process', views.process),

}
