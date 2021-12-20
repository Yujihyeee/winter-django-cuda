from django.conf.urls import url
from django.urls import path
from jeju_schedule import views

urlpatterns = {
    # url(r'pre', views.pre_process),
    url(r'upload', views.upload),
    path(r'recommendation', views.recommendation),
    path(r'days', views.days),
    path(r'save_days', views.save_days),

}
