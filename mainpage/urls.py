from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^index/(?P<pk>\d+)/$', views.index, name='index'),
    #기본도메인/main/index/(id번호)
]
