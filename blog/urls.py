from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', post_id, name='post_id'),
]
