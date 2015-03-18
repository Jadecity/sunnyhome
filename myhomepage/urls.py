from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import handler404

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sunnyhome.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^(?P<name>[a-z]*)/$','myhomepage.views.homepage'),
)

handler404 = 'myhomepage.views.page404'
