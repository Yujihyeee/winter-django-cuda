from django.conf.urls import url
from ledger import views

urlpatterns = {
    url(r'pre', views.preprocess),
    url(r'upload', views.upload),
    url(r'cost', views.cost)
}
