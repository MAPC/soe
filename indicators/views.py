from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from django.conf import settings
from indicators.models import TopicArea, Indicator

def index(request):
    
    topicareas = TopicArea.objects.filter(pub=True).order_by('order')
    
    return render_to_response('indicators/index.html', {
                                                        'topicareas': topicareas,
                                                        'base_url': settings.BASE_URL, }, 
                                                        context_instance=RequestContext(request))

def topicarea(request, topicarea_slug):
    
    topicareas = TopicArea.objects.filter(pub=True).order_by('order')
    
    # FIXME: query existing topicareas objects instead
    active_topicarea = TopicArea.objects.get(slug=topicarea_slug)
    
    return render_to_response('indicators/topicarea.html', {
                                                        'topicareas': topicareas,
                                                        'active_topicarea': active_topicarea,
                                                        'base_url': settings.BASE_URL, }, 
                                                        context_instance=RequestContext(request))

def indicator(request, topicarea, indicator):
    return HttpResponse('indicator view')