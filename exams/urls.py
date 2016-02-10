from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^full/$', views.index_full, name='index_full'),
    url(r'^(?P<exam_id>[^/]+)/$', views.exam, name='exam'),
    url(r'^subject/(?P<subject_id>[^/]+)/$', views.subject, name='subject')
]