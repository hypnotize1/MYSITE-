from importlib import simple
from django import template
from blog.models import post, Comment
from blog.models import Category

register = template.Library()


@register.simple_tag
def calculate():
     posts = post.objects.filter(status = 1).count()
     return posts


@register.simple_tag
def mypost():
     posts = post.objects.filter(status = 1)
     return posts


@register.filter
def snippets(value, arg = 12): 
     return value[:arg] + '...'


@register.inclusion_tag('blog/blog-latest.html')
def latestposts(arg = 4):
     posts = post.objects.filter(status = 1).order_by('published_date')[:arg]
     return {'posts' : posts}


@register.inclusion_tag('blog/blog-category.html')
def postcategory():
      cat_dt = {}
      posts = post.objects.filter(status = 1)
      cats = Category.objects.all()
      for name in cats:
           cat_dt[name] = posts.filter(category = name).count()

@register.simple_tag
def comments_count(pid):
     return Comment.objects.filter(Post = pid, approved = True).count()
