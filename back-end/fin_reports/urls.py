from django.conf.urls import url

from fin_reports import views

urlpatterns = [
    url(r'upload', views.upload)
]
