from django.conf.urls import url
from price import views

urlpatterns = {
    url(r'price', views.pre_price),

}
