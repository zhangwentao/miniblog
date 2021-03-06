from django.conf.urls.defaults import patterns, include, url
from blogs.views import test,draw,cross,artical,articalsInTag
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	(r'^draw/$',draw),
	(r'^$',test),
	(r'^crossdomain.xml$',cross),
	(r'^blog/(?P<id>\d+)/$',artical),
	(r'^articalsInTag/(?P<id>\d+)/$',articalsInTag),
)
