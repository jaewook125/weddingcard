"""wedding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.shortcuts import redirect

urlpatterns = [
    # url(r'^$', lambda r: redirect('mainpage:index'),name='root'),
    url(r'^admin/', admin.site.urls),
    url(r'^main/', include('mainpage.urls',namespace='mainpage')),
    url(r'^main2/', include('maincomment.urls',namespace='maincomment')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#어드민에서 사진 보기, 미디어 파일 서빙시키기
