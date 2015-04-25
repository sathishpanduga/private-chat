from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

from private_chat import views


urlpatterns = patterns('',
    url('^$', RedirectView.as_view(url=reverse_lazy('private-chat:profile')), name='index'),
    url('^profile/$', views.Profile.as_view(), name='profile'),
    url('^chats/(?P<username>.*?)/$', views.Chat.as_view(), name='chat'),
    url('^login/$', 'django.contrib.auth.views.login', kwargs={'template_name': 'private_chat/login.html'},
        name='login'),
)
