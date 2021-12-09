from django.conf.urls import url
from reservation import views

urlpatterns = {
    url(r'pre', views.preprocess),
    url(r'insert', views.insert_data),
}