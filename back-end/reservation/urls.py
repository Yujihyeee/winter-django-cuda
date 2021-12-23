from django.conf.urls import url
from reservation import views

urlpatterns = {
    url(r'pre', views.preprocess),
    url(r'insert', views.insert_data),
    url(r'invoice', views.show_invoice),
    url(r'process/(?P<pk>\w{0,50})$', views.process)
}
