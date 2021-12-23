from django.conf.urls import url
from image import views

urlpatterns = [
    url(r'upload', views.upload),
    url(r'all_db', views.all_upload),
]
