from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','meeting.views.index'),
    url(r'^register/$', 'meeting.views.register', name='register'),
    url(r'^login/$', 'meeting.views.user_login', name='login'),
    url(r'^logout/$', 'meeting.views.user_logout', name='logout'),
    url(r'^about/$', 'meeting.views.about', name='about'),
    url(r'^create-project/$', 'meeting.views.create_project', name='create-project'),
    url(r'^add-meeting/$', 'meeting.views.add_meeting', name='add-meeting'),
    url(r'^add-file/$', 'meeting.views.add_file', name='add-file'),
    url(r'^add-note/$', 'meeting.views.add_note', name='add-note'),
    url(r'^nav/', 'meeting.views.nav', name='navbar'),
)
