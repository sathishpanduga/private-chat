from django.conf.urls import patterns, url
from private_chat import views


urlpatterns = patterns('',
    url('^$', views.Index.as_view(), name='index'),
    url('^profile/$', views.Profile.as_view(), name='profile'),
    url('^login/$', 'django.contrib.auth.views.login', kwargs={'template_name': 'private_chat/login.html'},
        name='login'),
)
