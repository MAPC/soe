from django.db import models
from thumbs import ImageWithThumbsField
from tinymce import models as tinymce_models
from taggit.managers import TaggableManager

# Create your models here.

# workaround for South custom fields issues 
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ['^tinymce\.models\.HTMLField'])
    add_introspection_rules([], ['^indicators\.thumbs\.ImageWithThumbsField'])
except ImportError:
    pass

class TopicArea(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField('URL slug')
    overview = tinymce_models.HTMLField(null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    pub = models.BooleanField('Published')
    last_modified = models.DateTimeField(editable=False, auto_now=True)
    tags = TaggableManager()
    
    # So the model is pluralized correctly in the admin.
    class Meta:
        verbose_name_plural = 'Topic Areas'

    # Returns the string representation of the model.
    def __unicode__(self):
        return self.title
    
class Indicator(models.Model):
    topicarea = models.ForeignKey('indicators.Topicarea')
    title = models.CharField(max_length=50)
    slug = models.SlugField('URL slug',max_length=50)
    findings = tinymce_models.HTMLField(null=True, blank=True)
    impoimpl = tinymce_models.HTMLField('Importance and Implications', null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    pub = models.BooleanField('Published')
    last_modified = models.DateTimeField(editable=False, auto_now=True)
    tags = TaggableManager()
    
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
    caption = models.TextField(null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    pub = models.BooleanField('Published')
    last_modified = models.DateTimeField(editable=False, auto_now=True)
    tags = TaggableManager()
    
    # So the model is pluralized correctly in the admin.
    class Meta:
        verbose_name_plural = 'Graphs'

    # Returns the string representation of the model.
    def __unicode__(self):
        return self.title
    
class Reference(models.Model):
    number = models.IntegerField('Reference Number', unique=True)
    content = tinymce_models.HTMLField(null=True, blank=True)
    tags = TaggableManager()
    
    # So the model is pluralized correctly in the admin.
    class Meta:
        verbose_name_plural = 'References'
