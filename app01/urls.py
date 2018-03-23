"""project04_其他 URL Configuration

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

from app01 import views

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^index$',views.index),
    url(r'^upload$',views.upload),

    url(r'^do_upload$',views.do_upload),

    url(r'^show_images$',views.show_images),

    #显示页码的
    url(r'^show_page$',views.show_page),

    url(r'^show_page/(\d+)$', views.show_page),    # 分页显示区域
    #显示地区
    url(r'^show_areas$',views.shwo_areas),
    #json显示省份数据url
    url(r'^get_provinces$',views.get_provinces),
    #json显示省份数据url
    url(r'^get_children/(\d+)$', views.get_children),

]
