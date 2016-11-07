"""test1 URL Configuration

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
from django.conf.urls import url
from . import views

app_name = 'page_app'
urlpatterns = [

    url(r'^articles/(?P<id_art>\d+)?/?(?P<page_num>\d+)?/?$', views.article, name='article'),
    url(r'^reporters/$', views.reporter, name='reporters'),
    url(r'^reporters/(?P<id_rep>.*)/$', views.reporter, name='reporter'),
    url(r'^persons/(?P<id_pers>\d+)?/?(?P<page_num>\d+)?/?$', views.person, name='persone'),
    url(r'^test/(.*)/$', views.test, name='test'),
    url(r'^.*$', views.index, name='index')
    ]
#url(r'^articles/$', views.article, name='articles'),