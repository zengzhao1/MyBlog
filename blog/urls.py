from django.conf.urls import url

from . import  views

#声明此模块属于blog应用
#视图函数命名,防止冲突
app_name = 'blog'

urlpatterns = [
    url(r'^$',views.index, name = 'index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name = 'archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.category,name='category'),


]

