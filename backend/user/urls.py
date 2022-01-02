from django.conf.urls import url
from user import views

urlpatterns = {
    url(r'insert', views.insert_data),
    # url(r'mbti', views.count_mbti),
}
