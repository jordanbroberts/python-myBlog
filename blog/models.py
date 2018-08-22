from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
import datetime
from taggit.managers import TaggableManager

class Post(models.Model):

 title = models.CharField(max_length=200)
 image = models.CharField(max_length=400)
 content = HTMLField()
 created_on = models.DateTimeField(default=timezone.now) 
 category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True, related_name='allpost')
 author = models.ForeignKey( 'auth.User', on_delete=models.CASCADE,)
 tags = TaggableManager()
 
 def __str__(self):
          return self.title

class Category(models.Model):
 name= models.CharField(max_length=50)

 def __str__(self):
          return self.name
