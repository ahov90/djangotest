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
    url(r'^articles/?$', views.AllArticleView.as_view(), name='articles'),
    url(r'^articles/(?P<id_art>\d+)?/?(?P<page_num>\d+)?/?$', views.ArticleView.as_view(template_name = 'page/article.html'), name='article'),
    url(r'^reporters/$', views.AllReporterView.as_view(), name='reporters'),
    url(r'^reporters/(?P<id_rep>.*)/$', views.ReporterView.as_view(), name='reporter'),
    url(r'^persons/?$', views.AllPersonView.as_view(template_name = 'page/all_persons.html'), name='persones'),
    url(r'^persons/(?P<id_pers>\d+)?/?(?P<page>\d+)?/?$', views.PersonView.as_view(template_name = 'page/person.html'), name='persone'),
    # неименованная группа. Соответствует закомментированной строке в TestView self.test_list.append(self.args[0])
    #args и kwargs нельзя реализовывать в одной url. Для запуска неименованной группы надо ее раскоментировать и
    # закомментировать расположенную ниже
    #url(r'^testing/(\d+)/$', views.TestView.as_view(), name='testing'),
    url(r'^testing/(?P<test>\d+)/$', views.TestView.as_view(), name='testing'),
    url(r'^cbv/$',  views.CbvView.as_view(template_name = 'page/cbv.html'), name='cbv'),
    url(r'^.*$', views.index, name='index')
    ]

#(?P<test>.*)/