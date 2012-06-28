from django.conf.urls.defaults import patterns, include, url
from blogs.views import home,artical,articalsInTag,about,comment
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import accountbook.urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accountbook/',include('accountbook.urls')),
	(r'^$',home),
	(r'^comment$',comment),
	(r'^blog/(?P<id>\d+)/$',artical),
	(r'^articalsInTag/(?P<id>\d+)/$',articalsInTag),
	(r'^about/$',about),
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/home/wentao/Documents/lab/django/miniblog/templates'}),
)
