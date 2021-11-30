from django.conf.urls import url
from brevity import views

urlpatterns = {
    # url(r'pre', views.pre_process),
    url(r'upload', views.upload),

}
