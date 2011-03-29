from django.shortcuts import render_to_response
from django.template import RequestContext

from django.conf import settings
from models import TopicArea, Indicator, Reference

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

def indicator(request, topicarea_slug, indicator_slug):
    
    topicareas = TopicArea.objects.filter(pub=True).order_by('order')
    
    # FIXME: query existing topicareas objects instead
    active_topicarea = TopicArea.objects.get(slug=topicarea_slug)
    active_indicator = Indicator.objects.get(slug=indicator_slug)
    
    related_objects = active_indicator.tags.similar_objects()
    
    # return HttpResponse('OK')

    return render_to_response('indicators/indicator.html', {
                                                        'topicareas': topicareas,
                                                        'active_topicarea': active_topicarea,
                                                        'active_indicator': active_indicator,
                                                        'related_objects': related_objects,
                                                        'base_url': settings.BASE_URL, }, 
                                                        context_instance=RequestContext(request))

def reference(request, ref_id):
    
    topicareas = TopicArea.objects.filter(pub=True).order_by('order')
    
    reference = Reference.objects.get(number__iexact=ref_id)
    
    return render_to_response('indicators/reference.html', {
                                                        'reference': reference,
                                                        'topicareas': topicareas,
                                                        'base_url': settings.BASE_URL,}, 
                                                        context_instance=RequestContext(request))
    
def references(request):
    
    topicareas = TopicArea.objects.filter(pub=True).order_by('order')
    
    references = Reference.objects.all().order_by('number')
    
    return render_to_response('indicators/references.html', {
                                                        'references': references,
                                                        'topicareas': topicareas,
                                                        'base_url': settings.BASE_URL,}, 
                                                        context_instance=RequestContext(request))