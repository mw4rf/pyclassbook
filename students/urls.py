from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^full/$', views.index_full, name='index_full'),
    url(r'^show/(?P<student_id>[^/]+)/$', views.show, name='show')
]