from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<exam_id>[0-9]+)/$', views.exam, name='exam'),
    url(r'^/subject/(?P<subject_id>[0-9]+)/$', views.subject, name='subject')
]