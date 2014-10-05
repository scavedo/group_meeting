from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','meeting.views.index'),
    url(r'^register/$', 'meeting.views.register', name='register'),
    url(r'^login/$', 'meeting.views.user_login', name='login'),
    url(r'^logout/$', 'meeting.views.user_logout', name='logout'),
)
