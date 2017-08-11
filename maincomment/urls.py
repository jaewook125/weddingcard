from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^index2/(?P<pk>\d+)/$', views.index2, name='index2'),
    #기본도메인/main/index/(id번호)
    url(r'^comments/$', views.comment_list, name='comment_list'),
]
