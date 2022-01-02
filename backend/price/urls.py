from django.conf.urls import url
from price import views

urlpatterns = {
    url(r'price', views.pre_price),
    url(r'invoice', views.get_price),
    url(r'random', views.count_random),
}
