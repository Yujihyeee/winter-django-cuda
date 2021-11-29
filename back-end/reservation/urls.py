from django.conf.urls import url
from reservation import views

urlpatterns = {
    url(r'process', views.process),

}