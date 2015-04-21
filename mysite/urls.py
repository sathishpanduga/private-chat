from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^private-chat/', include('private_chat.urls', namespace='private-chat')),
    url(r'^admin/', include(admin.site.urls)),
)
