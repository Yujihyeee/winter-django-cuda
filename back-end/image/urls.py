from django.conf.urls import url
from image import views

urlpatterns = [
    url(r'upload', views.upload),

]