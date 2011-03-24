from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^soe/', include('soe.foo.urls')),
    (r'^$', 'indicators.views.index'),
    
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^tinymce/', include('tinymce.urls')),
    
    (r'^references/$', 'indicators.views.references'),
    (r'^references/(?P<ref_id>[-\w]+)/$', 'indicators.views.reference'),
    
    (r'^(?P<topicarea_slug>[-\w]+)/$', 'indicators.views.topicarea'),
    (r'^(?P<topicarea_slug>[-\w]+)/(?P<indicator_slug>[-\w]+)/$', 'indicators.views.indicator'),
    
)