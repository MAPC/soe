from django.shortcuts import render_to_response
from django.template import RequestContext

from django.conf import settings
from models import TopicArea, Indicator, Reference, Meta

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
    
    indicators = Indicator.objects.filter(pub=True, topicarea=active_topicarea).order_by('order')
    
    return render_to_response('indicators/topicarea.html', {
                                                        'topicareas': topicareas,
                                                        'indicators': indicators,
                                                        'active_topicarea': active_topicarea,
                                                        'base_url': settings.BASE_URL, }, 
                                                        context_instance=RequestContext(request))

def indicator(request, topicarea_slug, indicator_slug):
    
    topicareas = TopicArea.objects.filter(pub=True).order_by('order')
    
    # FIXME: query existing topicareas objects instead
    active_topicarea = TopicArea.objects.get(slug=topicarea_slug)
    active_indicator = Indicator.objects.get(slug=indicator_slug)
    
    indicators = Indicator.objects.filter(pub=True, topicarea=active_topicarea).order_by('order')
    
    related_objects = active_indicator.tags.similar_objects()
    
    # return HttpResponse('OK')

    return render_to_response('indicators/indicator.html', {
                                                        'topicareas': topicareas,
                                                        'indicators': indicators,
                                                        'active_topicarea': active_topicarea,
                                                        'active_indicator': active_indicator,
                                                        'related_objects': related_objects,
                                                        'base_url': settings.BASE_URL, }, 
                                                        context_instance=RequestContext(request))

def reference(request, ref_id):
    
    topicareas = TopicArea.objects.filter(pub=True).order_by('order')
    
    reference = Reference.objects.get(number__iexact=ref_id)
    
    meta_pages = Meta.objects.all()
    
    return render_to_response('indicators/reference.html', {
                                                        'reference': reference,
                                                        'meta_items': meta_pages,
                                                        'topicareas': topicareas,
                                                        'base_url': settings.BASE_URL,}, 
                                                        context_instance=RequestContext(request))
    
def references_index(request):
    
    topicareas = TopicArea.objects.filter(pub=True).order_by('order')
    
    meta_pages = Meta.objects.all()
    
    return render_to_response('indicators/references_index.html', {
                                                        'meta_items': meta_pages,
                                                        'topicareas': topicareas,
                                                        'base_url': settings.BASE_URL,}, 
                                                        context_instance=RequestContext(request))
    
def references_list(request):
    
    topicareas = TopicArea.objects.filter(pub=True).order_by('order')
    
    references = Reference.objects.all().order_by('number')
    
    meta_pages = Meta.objects.all()
    
    return render_to_response('indicators/references_list.html', {
                                                        'references': references,
                                                        'meta_items': meta_pages,
                                                        'topicareas': topicareas,
                                                        'base_url': settings.BASE_URL,}, 
                                                        context_instance=RequestContext(request))
    
def meta(request, meta_slug):
    
    topicareas = TopicArea.objects.filter(pub=True).order_by('order')
    
    meta_pages = Meta.objects.all()
    
    meta_page = Meta.objects.get(slug=meta_slug)
    
    return render_to_response('indicators/meta_page.html', {
                                                        'meta_page': meta_page,
                                                        'meta_items': meta_pages,
                                                        'topicareas': topicareas,
                                                        'base_url': settings.BASE_URL,}, 
                                                        context_instance=RequestContext(request))
    