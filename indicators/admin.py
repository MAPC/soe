from soe.indicators.models import TopicArea, Indicator, Graph, Reference
from django.contrib import admin

class TopicAreaAdmin(admin.ModelAdmin):
    list_display = ('title','pub')
    # list_filter = ['topicarea', 'inidcator']
    date_hierarchy = 'last_modified'
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('title','topicarea','pub')
    # list_filter = ['topicarea', 'inidcator']
    date_hierarchy = 'last_modified'
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    
class GraphAdmin(admin.ModelAdmin):
    list_display = ('title', 'topicarea','indicator')
    # list_filter = ['topicarea', 'inidcator']
    date_hierarchy = 'last_modified'
    search_fields = ['title']

admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(TopicArea, TopicAreaAdmin)
admin.site.register(Graph, GraphAdmin)
admin.site.register(Reference)