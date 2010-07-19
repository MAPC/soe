from soe.indicators.models import TopicArea, Indicator, Graph
from django.contrib import admin

class TopicAreaAdmin(admin.ModelAdmin):
    list_display = ('title',)
    # list_filter = ['topicarea', 'inidcator']
    date_hierarchy = 'last_modified'
    search_fields = ['title']
    
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('title','topicarea')
    # list_filter = ['topicarea', 'inidcator']
    date_hierarchy = 'last_modified'
    search_fields = ['title']

class GraphAdmin(admin.ModelAdmin):
    list_display = ('title', 'topicarea','indicator')
    # list_filter = ['topicarea', 'inidcator']
    date_hierarchy = 'last_modified'
    search_fields = ['title']

admin.site.register(Graph, GraphAdmin)
admin.site.register(Indicator)
admin.site.register(TopicArea, TopicAreaAdmin)