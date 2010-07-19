from django.db import models
from indicators.thumbs import ImageWithThumbsField
from tinymce import models as tinymce_models
# Create your models here.

class TopicArea(models.Model):
    title = models.CharField(max_length=50)
    overview = tinymce_models.HTMLField(null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    pub = models.BooleanField('Published')
    last_modified = models.DateTimeField(editable=False, auto_now=True)
    
    # So the model is pluralized correctly in the admin.
    class Meta:
        verbose_name_plural = 'Topic Areas'

    # Returns the string representation of the model.
    def __unicode__(self):
        return self.title

    
class Indicator(models.Model):
    topicarea = models.ForeignKey('indicators.Topicarea')
    title = models.CharField(max_length=50)
    findings = tinymce_models.HTMLField(null=True, blank=True)
    impoimpl = tinymce_models.HTMLField('Importance and Implications', null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    pub = models.BooleanField('Published')
    last_modified = models.DateTimeField(editable=False, auto_now=True)
    
    # So the model is pluralized correctly in the admin.
    class Meta:
        verbose_name_plural = 'Indicators'

    # Returns the string representation of the model.
    def __unicode__(self):
        return self.title
    
    
class Graph(models.Model):
    topicarea = models.ForeignKey('indicators.TopicArea', null=True, blank=True)
    indicator = models.ForeignKey('indicators.Indicator', null=True, blank=True)
    title = models.CharField(max_length=100)
    img = ImageWithThumbsField(upload_to='graphs', sizes=((125,125),(220,440)))
    caption = tinymce_models.HTMLField(null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    pub = models.BooleanField('Published')
    last_modified = models.DateTimeField(editable=False, auto_now=True)

    # So the model is pluralized correctly in the admin.
    class Meta:
        verbose_name_plural = 'Graphs'

    # Returns the string representation of the model.
    def __unicode__(self):
        return self.title
