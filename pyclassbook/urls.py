"""pyclassbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from home import views as home

urlpatterns = [
    url(r'^$', home.index, name='home'),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^admin/', include(admin.site.urls)),
    # Models
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^exams/', include('exams.urls', namespace='exams')),
    url(r'^courses/', include('courses.urls', namespace='courses')),
]