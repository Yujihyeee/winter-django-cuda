
from django.conf.urls import url

from jeju_data import views

urlpatterns = [
    url(r'upload', views.upload),

]