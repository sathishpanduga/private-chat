from django.conf.urls import patterns, url
from private_chat import views


urlpatterns = patterns('',
    url('^$', views.Index.as_view(), name='index'),
)
