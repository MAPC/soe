from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^soe/', include('soe.foo.urls')),
    (r'^$', 'soe.indicators.views.index'),
    
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^tinymce/', include('tinymce.urls')),
    
    # references
    (r'^references/$', 'soe.indicators.views.references_index'),
    (r'^references/(?P<ref_id>[-\d]+)/$', 'soe.indicators.views.reference'),
    (r'^references/list/$', 'soe.indicators.views.references_list'),
    (r'^references/(?P<meta_slug>[-\w]+)/$', 'soe.indicators.views.meta'),
    
    # topicareas and indicators
    (r'^(?P<topicarea_slug>[-\w]+)/$', 'soe.indicators.views.topicarea'),
    (r'^(?P<topicarea_slug>[-\w]+)/(?P<indicator_slug>[-\w]+)/$', 'soe.indicators.views.indicator'),
    
    
    
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$',
         'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True, }),
)