from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import handler404
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sunnyhome.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^myhomepage/', include('myhomepage.urls')),
#    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{
 #       'document_root':settings.),
  #  url(r'^media/$'),
    url(r'^admin/', include(admin.site.urls)),
)

handler404 = 'myhomepage.views.page404'
