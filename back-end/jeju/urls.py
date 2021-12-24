from django.conf.urls import url, re_path
from django.urls import path, re_path
from jeju import views_test, views

urlpatterns = [
    path(r'test_user', views_test.test_user),
    path(r'recommendation', views.recommendation),
    path(r'days', views.days),
    path(r'save_days', views.save_days),
    url(r'list/(?P<user_id>\w{0,500})$', views.list_by_user),
    url(r'pr_days/(?P<user_id>\w{0,500})$', views.list_by_user_pr),
    url(r'remove/(?P<pk>\w{0,500})$', views.del_list_by_user),
    path(r'update_dday', views.dday_up),
]

