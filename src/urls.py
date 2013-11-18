from django.conf.urls import patterns, include, url
from hikes.views import home, results, hike_detail, register
from django.contrib.auth.views import login, logout
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^results/$', results, name='results'),
    url(r'^hike/(?P<hike_id>\d+)/$', hike_detail, name='hike-detail'),
    url(r'^hike/(?P<hike_id>\d+)/(?P<slug>[-\w]+)/$', hike_detail, name='hike-detail'),
    url(r'^accounts/login/$', login, {'template_name':'login.html'}),
    url(r'^accounts/logout/$', logout, {'next_page': '/'}),
    url(r'^accounts/register/$', register),
    # url(r'^hikeplanner/', include('hikeplanner.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
