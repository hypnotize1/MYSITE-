from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name    

class post(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    image = models.ImageField(upload_to = 'blog-images/', default = 'blog-images/default.jpg')
    tags = TaggableManager()
    author = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    category = models.ManyToManyField(Category, )
    counted_views = models.IntegerField(default = 0)
    status = models.BooleanField(default = False)
    published_date = models.DateTimeField(null = True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True) 

    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return reverse('blog:single', kwargs = {'pid': self.id})
    
    
   